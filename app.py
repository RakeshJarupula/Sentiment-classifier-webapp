from flask import Flask, render_template, request, redirect
from load_model import load_and_predict
import gzip 
import joblib

app = Flask(__name__)

@app.route('/')
def main():
    return redirect('/index')

@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return 'This is Sentiment classification web app.'

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        text = request.args.get('text')
    else:
        text = request.form['text']
    
    with gzip.open('tfidf_transformer.pkl.gz', 'rb') as f:
        tfidf = joblib.open(f)
    
    with gzip.open('trained_model.pkl.gz', 'rb') as f:
        model = joblib.open(f)

    xt = tfidf.transform(text)
    proba = model.predict_proba([text])[0, 1]
    
    return 'Positive Sentiment with {}% confidance'.format(proba*100)


if __name__ =='__main__':
    app.run(debug=True)
