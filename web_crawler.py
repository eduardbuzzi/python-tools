import re
import requests

to_crawl = ['http://www.burgerking.com.br/']
crawled = set()

header = {'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) '
          'AppleWebKit/537.36 (KHTML, like Gecko) '
          'Chrome/83.0.4103.116 Mobile Safari/537.36'}

while True:
    url = to_crawl[0]
    try:
        req = requests.get(url, headers=header)
    except:
        to_crawl.remove(url)
        crawled.add(url)
        continue
    html = req.text

    links = re.findall(r'<a href="?\'?(https?:\/\/[^"\'>]*)', html)
    print 'Crawling: ', url

    to_crawl.remove(url)
    crawled.add(url)

    for link in links:
        if link not in crawled and link not in to_crawl:
            to_crawl.append(link)
