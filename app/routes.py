from flask import render_template, request, jsonify
from app import app
from app.sentiment_prediction import SentimentClassifier


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        classifier.is_alive()
    except:
        classifier = SentimentClassifier()

    pred = classifier.predict(request.form['txt'])

    return jsonify({'prediction': pred})
