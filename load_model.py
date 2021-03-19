def load_and_predict(text):
    import joblib
    import gzip
        
    with gzip.open('trained_model.pkl.gz', 'rb') as f:
        model = joblib.load(f)

    pred = model.predict_proba(text)[0, 1]
    pred = float(pred)
    if (pred > 0.5):
        return 'Positive Sentiment'
    else:
        return 'Negative Sentiment'
    

if __name__=='__main__':
    print(load_and_predict(['this is worst movie',]))