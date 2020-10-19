from my_module.crawler_setup import *
from my_module.db_conector import *

for urls in Url.where('status', 0).chunk(100):
    for url in urls:
        url.update(status=1)
        html = get_html(url.url)
        Html.insert({"url_id": url.id, "html": html})
        url.update(status=2)