"""requests para requisições HTTP"""

import requests

url = "http://127.0.0.1:5500/Secao%2006/aula190_site/index.html"
response = requests.get(url)
print(response.status_code)
print(response.text)
