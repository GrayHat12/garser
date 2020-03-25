from garser import Parser
import requests

r = requests.get('https://github.com/GrayHat12').text

p = Parser()
p.feed(r)
p.processElements()
element = p.getParentElement()
print(element)