import requests
import json

# proxies = {
#     'http'  :'http://www-proxy.us.oracle.com',
#     'https' :'http://www-proxy.us.oracle.com',
# }

url = r'https://www.omdbapi.com/?s=batman&apikey=b4e17ea0'
# r = requests.get(url, proxies = proxies)
r = requests.get(url)
if r.ok:
    data = json.loads(r.content)
    for movie in data['Search']:
        print movie['Title'], movie['imdbID']
        poster = movie['Poster']
        p = requests.get(poster)
        if p.ok:
            filename = 'posters\\' + movie['imdbID']+'.jpg'
            with open(filename, 'wb') as fh:
                fh.write(p.content)