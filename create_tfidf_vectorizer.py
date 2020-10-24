from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
from my_module.db_conector import *
from my_module.analyzer_setup import *

articles = Article.all()
article_ids = list(map(lambda x: x.id, articles))
article_texts = list(map(lambda x: x.title + x.summary + x.body, articles))

vectorizer = TfidfVectorizer(
    analyzer=analyzer,
    max_df=0.7
)

vectorizer.fit(article_texts)
bow = vectorizer.transform(article_texts)

with open('docs/vectorizer.pickle', 'wb') as f:
    pickle.dump(vectorizer, f)

with open('docs/bow.pickle', 'wb') as f:
    pickle.dump(bow, f)

with open('docs/article_ids.txt', 'w') as f:
    f.write(str(article_ids))