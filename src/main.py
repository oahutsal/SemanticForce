import requests
from lxml import etree
from io import StringIO, BytesIO

def save(obj):
    print(obj)

def parseUrl(url):
    resp = requests.get(url)
    parser = etree.HTMLParser()
    parsed = etree.parse(StringIO(resp.text), parser)
    root = parsed.getroot()
    article = {
        "title": root.xpath("/html/body/main/div/div[2]/div[2]/div/article/h1/text()")[0],
        "date": root.xpath("/html/body/main/div/div[2]/div[2]/div/article/div[1]/span/pre/a/text()")[0],
        "info": '\n'.join(list(root.xpath("//p/text()"))),
        "imageSrc": root.xpath("/html/body/main/div/div[2]/div[2]/div/article/div[2]/div[1]/a/img/@src")[0]
    }

    return article

def main():
    print('Start crawling...')
    article = parseUrl("https://112.ua/glavnye-novosti/v-kieve-muzhchina-ugrozhaet-vzorvat-bombu-v-bc-leonardo-vse-chto-izvestno-na-dannyy-moment-545095.html")
    save(article)

main()
