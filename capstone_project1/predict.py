from sentence_transformers import SentenceTransformer,util
from flask import Flask
from flask import request
import numpy as np
from flask import jsonify


app = Flask('dtc')

@app.route('/predict', methods=['POST'])
def predict():
    model = SentenceTransformer('all-MiniLM-L6-v2')

    data = request.get_json()

    candidate_answers = np.array(data['candidate_answers'])  # array of str
    question = np.array([data['question']]) # str

    q_emb = model.encode(question, show_progress_bar=True)
    ans_emb = model.encode(candidate_answers, show_progress_bar=True)

    sim = []
    for idx_, _ in enumerate(candidate_answers):
        print(idx_)
        print(q_emb[0])
        print(ans_emb[idx_])
        cos_sim = util.cos_sim(q_emb[0], ans_emb[idx_])
        sim.append(cos_sim.item())

    aidx = np.argmax(np.array(sim))

    return jsonify({'answer': candidate_answers[aidx]})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)
