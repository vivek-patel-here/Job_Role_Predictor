import re
import pickle
import pandas as pd;
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

df = pd.read_csv("data/raw/UpdatedResumeDataSet.csv")
print(df.head(5));

def clean_text(text):
    text = text.lower()  # lowercase
    text = re.sub(r'\S+@\S+', '', text)  # remove emails
    text = re.sub(r'http\S+', '', text)  # remove URLs
    text = re.sub(r'[^a-zA-Z ]', '', text)  # remove special chars
    text = re.sub(r'\s+', ' ', text)  # remove extra spaces
    return text

df['Resume'] = df['Resume'].apply(clean_text)

le = LabelEncoder()
df['Category'] = le.fit_transform(df['Category'])



X = df['Resume']
y = df['Category']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


tfidf = TfidfVectorizer(stop_words='english', max_features=3000)

X_train_tfidf = tfidf.fit_transform(X_train)
X_test_tfidf = tfidf.transform(X_test)

pickle.dump(X_train_tfidf, open("data/processed/X_train_tfidf.pkl", "wb"))
pickle.dump(X_test_tfidf, open("data/processed/X_test_tfidf.pkl", "wb"))
pickle.dump(y_train, open("data/processed/y_train.pkl", "wb"))
pickle.dump(y_test, open("data/processed/y_test.pkl", "wb"))
pickle.dump(le, open("data/processed/label_encoder.pkl", "wb"))
pickle.dump(tfidf, open("data/processed/tfidf_vectorizer.pkl", "wb"))