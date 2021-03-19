import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB

data = pd.read_csv('C:/Users/user/Desktop/ML-projects/Sentiment-classification-webapp/Dataset/IMDB Dataset.csv')
X = data['review'].copy()
y = data['sentiment']=='positive'
y = y.astype(int)

if __name__=='__main__':
    import gzip
    import joblib
    
    tfidf = TfidfVectorizer(stop_words='english', ngram_range=(1,2))
    pipe = Pipeline([('tfidf', tfidf), ('naive', MultinomialNB())])
    pipe.fit(X, y)
    print(f'Training accuracy:{pipe.score(X, y)}')
    
    with gzip.open('trained_model.pkl.gz', 'wb') as f:
        joblib.dump(pipe, f)
    