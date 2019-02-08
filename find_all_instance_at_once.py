import requests
from bs4 import BeautifulSoup
page = requests.get("https://www.simplilearn.com/top-ethical-hacking-certifications-to-consider-article")
print(page.status_code)
soup = BeautifulSoup(page.content,'html.parser')
soup.find_all('data-src')
i=0
for item in soup.find_all('img'):
	# print("ok")
	try:
		print(soup.find_all('img')[i]['src'])
		# i = str(i)
		f = open('0000000'+str(i)+'.jpg','wb')
		f.write(requests.get(soup.find_all('img')[i]['src']).content)
		f.close()
	except:
		print(soup.find_all('img')[i]['data-src'])
		# i= str(i)
		f = open('0000000'+str(i)+'.jpg','wb')
		f.write(requests.get(soup.find_all('img')[i]['data-src']).content)
		f.close()
	# break
	i = int(i)
	print("\n")
	i=i+1


print("#############################################################")
inputTag = soup.findAll(attrs={"data-src":"https://www.simplilearn.com/ice9/master_program/masters-badge-1.png"})
# print(inputTag[0])
