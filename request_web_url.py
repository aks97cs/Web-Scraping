import requests
page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
print(page) # Return status 200 for success

print(page.status_code) # Return status code

print(page.content) # Return page content code

