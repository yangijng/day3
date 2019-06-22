import requests
url = 'http://www.baidu.com/s?'
res=requests.get(url,params={'wd':'huoying'})
zz=print(res.text)
ress=zz.split('(')
for url in res :
    if 'http' in ress :
        res2 = url.split(')')
        print(res2 [0])
