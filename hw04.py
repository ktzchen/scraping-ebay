import requests
from bs4 import BeautifulSoup
import json

keyword = 'mug'
results = []

for i in range(1,11):
    #url = 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=' + keyword
    url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw=' + keyword + '&_sacat=0&_pgn=' + str(i)
    headers = { 
        'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:82.0) Gecko/20100101 Firefox/82.0'
    }    

    r = requests.get(url, headers=headers)

    print('r.status_code=', r.status_code)

    soup = BeautifulSoup(r.text, 'html.parser') #search html to extract individual items

    boxes = soup.select('.clearfix.s-item__wrapper') #.clearfix.s-item__wrapper or .clearfix.srp-list.srp-results > li.s-item
    for box in boxes:
        #print('=====')
        result = {}
        names = box.select ('.s-item__title')
        for name in names:
            #print('item=', title.text)
            result['name'] = name.text
        prices = box.select ('.s-item__price')
        for price in prices:
            #print('price=', price.text)
            result['price'] = price.text
        statuses = box.select ('.SECONDARY_INFO')
        for status in statuses:
            #print('status=', status.text)
            result['status'] = status.text
        results.append(result)
        #print('result=', result)


    print('len of results=', len(results))

j = json.dumps(results)
with open('items.json', 'w') as f:
    f.write(j) 