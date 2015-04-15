

import requests
from lxml import html
import csv

error_log = open('error.log', 'a')


urls = [
	'http://www.thofood.com/Home/ProductList?BClass=244cb8e5548c40288b88bb43317e0cb9',
	'http://www.thofood.com/Home/ProductList?BClass=23f8874856f94e48b26ff4483e46e6a0',
	'http://www.thofood.com/Home/ProductList?BClass=bc4bd75906cf423483e41ff8b3f51e9a',
	'http://www.thofood.com/Home/ProductList?BClass=df7f70252a3d4999b29c79df3745d3f4',
	'http://www.thofood.com/Home/ProductList?BClass=f46f2923ba724a1c87a4d4ca991c985f',
]

index = 0
with open('thofood.csv', 'w') as csvfile:
	fieldnames = ['link', 'name','price']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	for url in urls:
		content = requests.get('http://www.thofood.com/Home/ProductList?BClass=244cb8e5548c40288b88bb43317e0cb9')
		tree = html.fromstring(content.text)
		img = tree.xpath('//div[@class="right"]/div[@class="sort_list"]/ul/li[@class="img"]/a/img')
		name = tree.xpath('//div[@class="right"]/div[@class="sort_list"]/ul/li[@class="name"]/a/text()')
		price = tree.xpath('//div[@class="right"]/div[@class="sort_list"]/ul/li[@class="money"]/span/text()')
		for i,img in enumerate(img):
			print index
			index += 1
			writer.writerow({
				'link': u'http://www.thofood.com%s' % img.attrib['src'].encode('utf-8').decode('big5'),
				'name': name[i].encode('big5','ignore'),
				'price': price[i].encode('big5','ignore')
			})