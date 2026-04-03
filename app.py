from flask import Flask, request,jsonify
import pickle
import re

app = Flask(__name__)

model = pickle.load(open("model/model.pkl", "rb"))
le = pickle.load(open("data/processed/label_encoder.pkl", "rb"))
tfidf = pickle.load(open("data/processed/tfidf_vectorizer.pkl", "rb"))
def clean_text(text):
    text = text.lower()  # lowercase
    text = re.sub(r'\S+@\S+', '', text)  # remove emails
    text = re.sub(r'http\S+', '', text)  # remove URLs
    text = re.sub(r'[^a-zA-Z ]', '', text)  # remove special chars
    text = re.sub(r'\s+', ' ', text)  # remove extra spaces
    return text


# Index Route
@app.route("/",methods=['GET','POST'])
def index():
    if(model and le and tfidf):
        print("All set.")
    else:
        print("Some Issue is there!")
    print("Server is running on port 5000.")
    return {"status":200,
            "message":"Server is running healthy."
        }

# main EndPoint
@app.route("/resume/predict", methods=["POST"])
def predict():
    data = request.get_json()

    resume_text = data.get("resume", "")
    resume_text = clean_text(resume_text)

    # Transform input
    vector = tfidf.transform([resume_text])

    # Predict
    prediction = model.predict(vector)
    role = le.inverse_transform(prediction)[0]

    probs = model.predict_proba(vector)
    confidence = max(probs[0]) * 100

    job_role = data.get("job_role", "")
    score = 50
    if role.lower() == job_role.lower():
        score += confidence
    else:
        score += confidence * 0.8
    return jsonify({
        "predicted_role": role,
        "match_score": min(score,98)
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)