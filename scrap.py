from lxml import html
import requests

page = requests.get('http://www.parliament.go.tz/index.php/home/pages/44')
tree = html.fromstring(page.text)



