def load_and_predict(text):
    import joblib
    import gzip
        
    with gzip.open('trained_model.pkl.gz', 'rb') as f:
        model = joblib.load(f)

    pred = model.predict(text)
    print(pred)
    if pred == 1:
        return 'Positive Sentiment'
    else:
        return 'Negative Sentiment'
    

if __name__=='__main__':
    load_and_predict(input('Enter your text:'))