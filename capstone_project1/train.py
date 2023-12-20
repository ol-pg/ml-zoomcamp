import pandas as pd
import numpy as np
import re
from tqdm.auto import tqdm
from sentence_transformers import SentenceTransformer,util



data_path = '/Users/olga/github/ml-zoomcamp/capstone_project1/data/'
train_questions_df = pd.read_csv(f'{data_path}/train_questions.csv')
train_answers_df = pd.read_csv(f'{data_path}/train_answers.csv')

train_merged_df = pd.merge(train_questions_df, train_answers_df,
                           on='answer_id',
                           how='inner',
                           suffixes=('_question', '_answer'))

train_merged_df = train_merged_df.drop_duplicates(subset=['question'])

def clean_text(text):
    text = re.sub(r'[^\w\s]', '', text)
    text = text.lower()
    return text

train_merged_df['cleaned_question'] = train_merged_df['question'].apply(clean_text)
train_merged_df['cleaned_answer'] = train_merged_df['answer'].apply(clean_text)

# # Model training

model = SentenceTransformer('all-MiniLM-L6-v2')
train_merged_df["candidate_answers"] = train_merged_df["candidate_answers"].str.split(",")

q_emb = model.encode(train_merged_df["cleaned_question"].values,show_progress_bar=True)
ans_emb = model.encode(train_merged_df["cleaned_answer"].values,show_progress_bar=True)

train_ans_dict = {}
for idx,(_,row) in enumerate(tqdm(train_merged_df.iterrows(),total=len(train_merged_df))):
    train_ans_dict[f"{row['answer_id']}"] = ans_emb[idx]

preds = []
for idx,(_,row) in enumerate(tqdm(train_merged_df.iterrows(),total=len(train_merged_df))):
    if idx != -1:
        sim = []
        for ca in row["candidate_answers"]:
            cos_sim = util.cos_sim(q_emb[idx],train_ans_dict[f"{ca}"])
            sim.append(cos_sim.item())
        aidx = np.argmax(np.array(sim))
        preds.append(row["candidate_answers"][aidx])

preds = np.array(preds)
