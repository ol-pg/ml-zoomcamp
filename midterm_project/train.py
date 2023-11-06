import pandas as pd
import numpy as np

from sklearn.metrics import mutual_info_score, confusion_matrix, roc_auc_score, roc_curve, ConfusionMatrixDisplay
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction import DictVectorizer
from sklearn.preprocessing import OneHotEncoder

import pickle


output_file = 'model.bin'

df = pd.read_csv('tiktok_dataset.csv')
df.columns=df.columns.str.lower().str.replace(' ','_')

df = df.dropna(axis=0)
df=df.drop_duplicates()


# # Model training

X = df.copy()
X = X.drop(['#', 'video_id', 'video_like_count'], axis=1)
X['claim_status'] = X['claim_status'].replace({'opinion': 0, 'claim': 1})
X['text_length'] = X['video_transcription_text'].str.len()
col_encode = OneHotEncoder(drop='first').fit(X[['verified_status', 'author_ban_status']])
col_encode_transformed = col_encode.transform(X[['verified_status', 'author_ban_status']]).toarray()

ohe_df = pd.DataFrame(col_encode_transformed, columns=col_encode.get_feature_names_out())
X = pd.concat([X, ohe_df], axis=1).drop(['verified_status', 'author_ban_status'], axis=1)


y = X['claim_status']
X = X.drop(['claim_status'], axis=1)

X_full_train, X_test, y_full_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
X_train, X_valid, y_train, y_valid = train_test_split(X_full_train, y_full_train, test_size=0.25, random_state=0)


# ### Tokenize text column

count_vector = CountVectorizer(ngram_range=(2, 3),
                            max_features=15,
                            stop_words='english')

count_array = count_vector.fit_transform(X_train['video_transcription_text']).toarray()
count_df = pd.DataFrame(data=count_array, columns=count_vector.get_feature_names_out())
X_train_new = pd.concat([X_train.drop(columns=['video_transcription_text']).reset_index(drop=True), 
                         count_df], axis=1)


validation_count_array = count_vector.transform(X_valid['video_transcription_text']).toarray()
validation_count_df = pd.DataFrame(data=validation_count_array, columns=count_vector.get_feature_names_out())
X_valid_new = pd.concat([X_valid.drop(columns=['video_transcription_text']).reset_index(drop=True), 
                         validation_count_df], axis=1)


test_count_array = count_vector.transform(X_test['video_transcription_text']).toarray()
test_count_df = pd.DataFrame(data=test_count_array, columns=count_vector.get_feature_names_out())
X_test_new = pd.concat([X_test.drop(columns=['video_transcription_text']).reset_index(drop=True), 
                          test_count_df], axis=1)



# ## Random Forest

rf = RandomForestClassifier(random_state=0)

cv_params = {'max_depth': [5, 7, None],
             'max_features': [0.3, 0.6],
             'max_samples': [0.7],
             'min_samples_leaf': [1,2],
             'min_samples_split': [2,3],
             'n_estimators': [75,100,200]}

scoring = ['accuracy', 'precision', 'recall', 'f1']

rf_cv = GridSearchCV(rf, cv_params, scoring=scoring, cv=5, refit='recall')
rf_cv.fit(X_train_new, y_train)


y_predict = rf_cv.best_estimator_.predict(X_valid_new)

print(rf_cv.best_score_)

with open(output_file,'wb') as f_out:
    pickle.dump((count_vector, col_encode, rf_cv),f_out)

print(f'the model is saved to {output_file}')



