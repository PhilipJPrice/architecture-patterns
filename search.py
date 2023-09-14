# Do a search with urllib

import json
from urllib.request import urlopen
from urllib.parse import urlencode

print("Search with urllib: ")
print("")

params = dict(q='Sausages', format='json')
handle = urlopen('http://api.duckduckgo.com' + '?' + urlencode(params))
raw_text = handle.read().decode('utf8')
parsed = json.loads(raw_text)

results = parsed['RelatedTopics']
for r in results:
    if 'Text' in r:
        print(r['FirstURL'] + ' - ' + r['Text'])

print("")
print("")

# Do a search with requests

import requests

print("Search with requests: ")
print("")

params = dict(q='Sausages', format='json')
parsed = requests.get('http://api.duckduckgo.com/', params=params).json()
results = parsed['RelatedTopics']
for r in results:
    if 'Text' in r:
        print(r['FirstURL'] + ' - ' + r['Text'])


print("")
print("")

# Do a search with the duckduckgo client library

import duckduckpy

print("Search with duckduckgo library: ")
print("")

for r in duckduckpy.query('Sausages').related_topics:
    print(r.first_url, ' - ', r.text)
