from sklearn.externals import joblib


class SentimentClassifier:
    def __init__(self):
        self.model = joblib.load(open('app/model/model.pkl', 'rb'))
        self.vectorizer = joblib.load(open('app/model/vectorizer.pkl', 'rb'))
        self.data = ''
        self.prediction = ''

    @staticmethod
    def is_alive():
        return True

    def predict(self, text):
        self.data = self.vectorizer.transform([text])
        self.prediction = self.model.predict(self.data)[0]

        if self.prediction == -1:
            return 'negative'
        elif self.prediction == 1:
            return 'positive'
        else:
            return 'prediction error...'
