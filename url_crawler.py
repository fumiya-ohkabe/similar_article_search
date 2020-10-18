from my_module.crawler_setup import *
from my_module.db_conector import *

def create_url_model(soup):
    article_blocks = soup.select(".article_list_content")

    for article_block in article_blocks:
        obj = {}
        obj["url"] = article_block.select(".article_list_title > a")[0]["href"]
        obj["loves"] = article_block.select(".article_list_like")[0].get_text()
        obj["views"] = obj["views"] = article_block.select(".article_list_view")[0].get_text().replace("view", "").replace("｜", "")
        Url.insert(obj)


# for i in range(1, 9999):
for i in range(1, 750):
    url = f"https://mery.jp/search?page={i}"
    html = get_html(url)
    soup = BeautifulSoup(html, 'html.parser')

    # 検索結果を最後のページまでクロールした時の処理
    if soup.select(".m-errorPage"):
        break

    create_url_model(soup)