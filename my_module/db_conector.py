from orator import DatabaseManager, Model

config = {
    'mysql': {
        'driver': 'mysql',
        'host': 'localhost',
        'database': 'similar_article_search',
        'user': 'root',
        'charset': 'utf8mb4',
        'password': '',
        'prefix': ''
    }
}

db = DatabaseManager(config)
Model.set_connection_resolver(db)


class Url(Model):
    __guarded__ = [None]

class Html(Model):
    __guarded__ = [None]

class Article(Model):
    __guarded__ = [None]
