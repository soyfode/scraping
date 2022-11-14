import requests

headers = {
    "user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36",
    "referer":"https://www.emol.com/"
        }

url_api = 'https://cache-comentarios.ecn.cl/Comments/Api?action=getMostCommentedPages&site=emol&siteSection=nacional&format=json'

request = requests.get(url_api, headers=headers)

data = request.json()

for i in range(0, len(data)):
    print(data[i]["title"])
    print(data[i]["publicationDate"])
    print(data[i]["siteSection"])
