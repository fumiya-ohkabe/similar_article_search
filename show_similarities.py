from sklearn.metrics.pairwise import cosine_similarity
import collections
import pickle
import json

def show_similarities(text):
    with open('docs/article_ids.txt', 'r') as f:
        article_ids = json.load(f)

    with open('docs/vectorizer.pickle', 'rb') as f:
        vectorizer = pickle.load(f)

    with open('docs/bow.pickle', 'rb') as f:
        bow = pickle.load(f)

    # 分析したいテキストと既存のテキストのコサイン類似度を出す
    new_text = [text]
    new_bow = vectorizer.transform(new_text)
    sim_matrix = cosine_similarity(new_bow, bow)

    # 類似度上位20件をid付きで返す
    ids_with_sims = [{"id": id , "similarity": sim} for id, sim in zip(article_ids, sim_matrix[0])]
    sorted_ids_with_sims = sorted(ids_with_sims, key=lambda x: x["similarity"], reverse=True)
    return sorted_ids_with_sims[0:20]

if __name__ == '__main__':
    sample_text = "レディースのセットアップコーデにスニーカーを合わせればこなれ感のあるコーデに。"
    similarities = show_similarities(sample_text)
    print(similarities)