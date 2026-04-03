import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

model = LogisticRegression(max_iter=1000)


X_train_tfidf  = pickle.load(open("data/processed/X_train_tfidf.pkl","rb"))
X_test_tfidf  = pickle.load(open("data/processed/X_test_tfidf.pkl","rb"))
y_train  = pickle.load(open("data/processed/y_train.pkl","rb"))
y_test  = pickle.load(open("data/processed/y_test.pkl","rb"))


model.fit(X_train_tfidf, y_train)
y_pred = model.predict(X_test_tfidf)


print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# save model
pickle.dump(model, open("model/model.pkl", "wb"))