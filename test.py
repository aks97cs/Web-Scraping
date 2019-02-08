import requests
f = open('00000001.jpg','wb')
f.write(requests.get('http://www.gunnerkrigg.com//comics/00000001.jpg').content)
f.close()