#!/usr/bin/python
from lxml import html
import requests

url = raw_input(">").split()
 
page = requests.get('urlo')
tree = html.fromstring(page.content)

print(tree)
print(page.content)


