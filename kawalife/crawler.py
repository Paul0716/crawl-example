#! bin/bash

import requests
from lxml import html
import csv

error_log = open('sjpork_error.log', 'a')


content = requests.get('http://www.kawalife.com/speclist.php')
tree = html.fromstring(content.text)
p = tree.xpath('//form[@name="form1"]/table/tbody/td/tr')

print p


# with open('sjpork.csv', 'w') as csvfile:
# 	fieldnames = ['link', 'name','unit','price']
# 	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
# 	for i,img in enumerate(product_img):
# 		print img.attrib['src'].encode('utf-8')
# 		print product_name[i]
# 		print product_unit[i]
# 		print product_price[i]
# 		writer.writerow({
# 			'link': u'http://www.sjpork.com.tw%s' % img.attrib['src'].encode('utf-8').decode('big5'),
# 			'name': product_name[i].encode('big5','ignore'),
# 			'unit': product_unit[i].encode('big5','ignore'),
# 			'price': product_price[i].encode('big5','ignore')
# 		})
