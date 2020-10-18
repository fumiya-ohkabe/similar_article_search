import requests
from bs4 import BeautifulSoup
import time

def get_html(url):
    time.sleep(1)
    res = requests.get(url)
    return res.text