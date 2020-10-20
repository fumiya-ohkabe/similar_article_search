from my_module.crawler_setup import *
from my_module.db_conector import *
import json
import urllib.parse

def basic_feature(html_record, url_record):
    ret = {}
    ret["html_id"]              = html_record.id
    ret["link"]                 = url_record.url
    ret["views"]                = url_record.views
    ret["loves"]                = url_record.loves
    return ret

def parse_writer_name(soup):
    curator_json = soup.select("[type='application/ld+json']")[0].string
    curator_dict = json.loads(curator_json)
    writer_name = curator_dict["author"]["name"]
    return writer_name

def parse_writer_link(soup):
    curator_json = soup.select("[type='application/ld+json']")[0].string
    curator_dict = json.loads(curator_json)
    curator_image = curator_dict["author"]["image"]["url"]
    query = urllib.parse.urlparse(curator_image).query
    curator_image_2 = urllib.parse.parse_qs(query)["url"][0]
    curator_id = curator_image_2.split("/")[4]
    writer_link = f"https://mery.jp/users/{curator_id}"
    return writer_link

def parse_category(soup):
    category_json = soup.select("[type='application/ld+json']")[1].string
    category_dict = json.loads(category_json)
    category = category_dict["itemListElement"][-1]["item"]["name"]
    return category

def parse_detail_feature(soup):
    ret = {}
    ret["html_id"]              = html.id
    ret["link"]                 = url_record.url
    ret["views"]                = url_record.views
    ret["loves"]                = url_record.loves
    ret["title"]                = soup.select("h1")[0].get_text().strip()
    ret["summary"]              = soup.select(".articleLead")[0].get_text().strip()
    ret["body"]                 = "".join([c.get_text() for c in soup.select(".article_content")])
    ret["writer_name"]          = parse_writer_name(soup)
    ret["writer_link"]          = parse_writer_link(soup)
    ret["category"]             = parse_category(soup)
    ret["article_published_at"] = soup.select(".article-date")[0].get_text().strip().split("\n")[1].strip().replace("作成：", "")
    ret["article_modified_at"]  = soup.select(".article-date")[0].get_text().strip().split("\n")[0].replace("更新：", "")
    return ret

while True:
    html = Html.where('status', 0).first()
    if html == None:
        break

    html.update(status=1)
    url_record = Url.where("id", html.url_id).first()
    bf_dict = basic_feature(html, url_record)
    soup = BeautifulSoup(html.html, 'html.parser')
    df_dict = parse_detail_feature(soup)
    features = {**bf_dict, **df_dict}
    Article.insert(features)
    html.update(status=2)
