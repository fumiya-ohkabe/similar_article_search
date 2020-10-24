from bottle import route, get, post, request, run
import jinja2
from bottle import TEMPLATE_PATH, jinja2_template as template
from my_module.db_conector import *
from show_similarities import *

TEMPLATE_PATH.append("./template")

@route('/', method=["GET"])
def toppage():
    return template('search.j2')

@route('/search', method=["GET", "POST"])
def get_article():
    text = request.forms.article_text

    # 入力テキストとの類似度を計算し記事idと類似度のlist of dictを返す
    similarities = show_similarities(text)

    # DBからarticleレコードを取得するための処理
    article_ids = [sim["id"] for sim in similarities]
    articles = Article.where_in('id', article_ids).get().serialize()

    # similaritiesとarticlesをjoinするための処理。similaritiesは破壊的に処理されている。
    for similarity in similarities:
        target_article = [article for article in articles if article["id"] == similarity["id"]][0]
        similarity.update(target_article)

    return template('search_result.j2', results=similarities)


run(host='localhost', port=8080, debug=True, reloader=True)
