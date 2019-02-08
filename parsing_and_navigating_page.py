import requests
from bs4 import BeautifulSoup
page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
soup = BeautifulSoup(page.content,'html.parser')
# print(soup) # return html code
# print(soup.prettify()) # return structured html code
# print("############################################")
# print(list(soup.children))

# print("listing soup children..........")
# for item in list(soup.children):
# 	print(type(item))

html = list(soup.children)[2]
# # print(html)
# i=0
# for item in list(soup.children):
# 	print("for i = ",i)
# 	print(list(soup.children)[i])
# 	i = i+1
print(list(html.children))
# body = list(soup.children)[3]
# print(body)
i=0
for item in list(html.children):
	print("for i = ",i)
	print(list(html.children)[i])
	i = i+1
body = list(html.children)[3]

print("element in body")
i=0
for item in list(body.children):
	print("for i = ",i)
	print(list(body.children)[i])
	i = i+1

para = list(body.children)[1]

print(para.get_text())