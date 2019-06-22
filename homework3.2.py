import requests
response=requests.get('http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02127808')
HTML=response.text
name = HTML.split('\n')
for url in name:
    try:
        name1 = requests.get(url=url,timeout=3)
    except :
        print(timeout)
    if name2 = url.split('/')[-1]:
        with open(nmae2,'wb') as f:
            f.write(picture.content)
