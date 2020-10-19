from my_module.crawler_setup import *
from my_module.db_conector import *
import json
import urllib.parse

for htmls in Html.where('status', 0).chunk(100):
    for html in htmls:
        html.update(status=1)
        soup = BeautifulSoup(html.html, 'html.parser')
        obj = {}
        obj["html_id"]              = html.id
        obj["title"]                = soup.select("h1")[0].get_text().strip()
        obj["summary"]              = soup.select(".articleLead")[0].get_text().strip()
        obj["body"]                 = "".join([c.get_text() for c in soup.select(".article_content")])

        curator_json = soup.select("[type='application/ld+json']")[0].string
        curator_dict = json.loads(curator_json)
        obj["writer_name"]          = curator_dict["author"]["name"]

        curator_image = curator_dict["author"]["image"]["url"]
        query = urllib.parse.urlparse(curator_image).query
        curator_image_2 = urllib.parse.parse_qs(query)["url"][0]
        curator_id = curator_image_2.split("/")[4]
        obj["writer_link"]          = f"https://mery.jp/users/{curator_id}"

        category_json = soup.select("[type='application/ld+json']")[1].string
        category_dict = json.loads(category_json)
        obj["category"]             = category_dict["itemListElement"][-1]["item"]["name"]

        obj["article_published_at"] = soup.select(".article-date")[0].get_text().strip().split("\n")[1].strip().replace("作成：", "")
        obj["article_modified_at"]  = soup.select(".article-date")[0].get_text().strip().split("\n")[0].replace("更新：", "")
        Article.insert(obj)

        html.update(status=2)