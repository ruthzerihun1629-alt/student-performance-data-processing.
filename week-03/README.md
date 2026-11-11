Week 03: SMS Spam Filter
Project Overview
This project builds an SMS spam classifier using the SMS Spam Collection dataset. It uses TF-IDF to convert text messages into numerical features and Multinomial Naive Bayes to classify messages as spam or ham (normal).

The project also tests five manually written messages to observe how the classifier handles unusual spelling, misleading wording, and ordinary messages containing words that may appear in spam.
Dataset
- Dataset: SMS Spam Collection
- Source: UCI Machine Learning Repository – SMS Spam Collection
- Records: 5,572 SMS messages
- Labels: ham and spam
The dataset file is not included in this repository. Download and extract the dataset, then place SMSSpamCollection in the data/ folder.
Project Structure
week-03/
├── data/
│   └── SMSSpamCollection
├── spam_filter.py
├── spam_filter.ipynb
├── README.md
└── requirements.txt

Technologies Used
- Python
- Pandas
- Scikit-learn
- TF-IDF Vectorizer
- Multinomial Naive Bayes
- Jupyter Notebook / Google Colab

How It Works
1. Load the SMS messages and their labels.
2. Split the dataset into 80% training data and 20% testing data.
3. Use TfidfVectorizer to convert text messages into numerical features.
4. Train a MultinomialNB classifier.
5. Predict labels for the test data and calculate accuracy.
6. Test five additional messages designed to challenge the classifier.

Model Evaluation
The model achieved 96.68% accuracy on the held-out test set using test_size=0.2 and random_state=42.
Evaluation	Result
Training data	80%
Testing data	20%
Vectorizer	TF-IDF
Classifier	Multinomial Naive Bayes
Accuracy	96.68%


Testing Messages
My message	Model said	Should be	Why it failed / result
Cl@im your fr33 g1ft card now!	ham	spam	Incorrect. Replacing letters with symbols and numbers changes familiar words into forms the model may not have learned.
Not free, just confirming lunch at 1pm.	ham	ham	Correct. The model recognized this ordinary message as ham, even though it contains the word “free.”
Congratulations! Your account has been selected for a cash reward.	spam	spam	Correct. The message contains wording and terms commonly associated with spam.
Hey, can you send me the meeting link?	ham	ham	Correct. The model correctly classified this ordinary request as ham.
WIN a prize now! Reply STOP if you are not interested.	ham	spam	Incorrect. The model did not recognize this combination of promotional wording as spam. It learns statistical word patterns, not the full meaning or intention of a message.


Manual test result: 3 out of 5 messages were classified as expected (60%). This is separate from the model's 96.68% accuracy on the held-out test set.
What I Learned
I learned how to use TF-IDF to convert text messages into numerical features and how a Multinomial Naive Bayes model can classify messages as spam or ham. I also learned that a model with high test accuracy can still make mistakes on new messages, especially when words are modified or the message uses patterns it did not learn well during training.

How to Run
1. Download and extract the SMS Spam Collection dataset from the UCI link above.
2. Put SMSSpamCollection inside the data/ folder.
3. Install the required packages:
pip install -r requirements.txt
4. Run the Python script:
python spam_filter.py
The notebook spam_filter.ipynb contains the code, outputs, and explanations for the assignment.