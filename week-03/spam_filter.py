from pathlib import Path

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

DATA_PATH = Path(__file__).parent / "SMSSpamCollection"

df = pd.read_csv(
    DATA_PATH,
    sep="\t",
    header=None,
    names=["label", "message"]
)

emails = df["message"]
labels = df["label"]

X_train, X_test, y_train, y_test = train_test_split(
    emails, labels, test_size=0.2, random_state=42
)

vec = TfidfVectorizer()
model = MultinomialNB()
model.fit(vec.fit_transform(X_train), y_train)

predictions = model.predict(vec.transform(X_test))
accuracy = accuracy_score(y_test, predictions)

print(f"Model accuracy: {accuracy * 100:.2f}%")

tests = [
    "Cl@im your fr33 g1ft card now!",
    "Not free, just confirming lunch at 1pm.",
    "Congratulations! Your account has been selected for a cash reward.",
    "Hey, can you send me the meeting link?",
    "WIN a prize now! Reply STOP if you are not interested."
]

test_vectors = vec.transform(tests)
test_predictions = model.predict(test_vectors)

print("\nTest message predictions:")
for message, prediction in zip(tests, test_predictions):
    print(f"Message: {message}")
    print(f"Model prediction: {prediction}")
    print()
