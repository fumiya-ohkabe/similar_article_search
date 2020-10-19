from bottle import route, get, post, request, run
import jinja2
from bottle import TEMPLATE_PATH, jinja2_template as template
from my_module.db_conector import *

TEMPLATE_PATH.append("./template")

@route('/', method=["GET"])
def toppage():
    return template('search.j2')

@route('/search', method=["GET", "POST"])
def get_article():
    r = request.forms.get('article_text')
    similar_article_ids = list(range(1, 100))
    results =Article.where_in('id', similar_article_ids).get().serialize()
    return template('search_result.j2', results=results)


run(host='localhost', port=8080, debug=True, reloader=True)
