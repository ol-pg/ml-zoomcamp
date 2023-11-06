import pickle
import pandas as pd
from flask import Flask
from flask import request
from flask import jsonify

model_file='model.bin'

with open(model_file,'rb') as f_in:
    count_vector, col_encode, rf_cv = pickle.load(f_in)

app = Flask('tik_tok')

@app.route('/predict',methods=['POST'])
def predict():

    status=request.get_json() 
    
    status=pd.DataFrame([status])
    X = status.copy()
    X = X.drop(['#', 'video_id', 'video_like_count'], axis=1)
    X['text_length'] = X['video_transcription_text'].str.len()
    col_encode_transformed = col_encode.transform(X[['verified_status', 'author_ban_status']]).toarray()
    ohe_df = pd.DataFrame(col_encode_transformed, columns=col_encode.get_feature_names_out())
    X = pd.concat([X, ohe_df], axis=1).drop(['verified_status', 'author_ban_status'], axis=1)
    
    print(X.columns)
    
    transcription_text = count_vector.transform(X['video_transcription_text']).toarray()
    transcription_text_df = pd.DataFrame(data=transcription_text, columns=count_vector.get_feature_names_out())
    X_final = pd.concat([X.drop(columns=['video_transcription_text']).reset_index(drop=True), 
                              transcription_text_df], axis=1)
    
    y_pred=rf_cv.best_estimator_.predict(X_final) 
    
    print(y_pred)
    
    result={
        'claim_status:': 'claim' if y_pred[0] == 1 else 'opinion'
    }
    return jsonify(result)


if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=9696)