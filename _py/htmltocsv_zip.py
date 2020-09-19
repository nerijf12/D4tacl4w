from lxml import html
import requests
import csv

zipcode = "zipcode.csv"
page = requests.get('http://bexar.trueautomation.com/clientdb/Property.aspx?cid=110&prop_id=1275766')
table = html.fromstring(page.content)
index = 0
startingNum = 2

#This will create a list of buyers:
taxrate = table.xpath('//table[@class="tableData"]/tr/td//text()')
#This will create a list of prices
description = table.xpath('//tr/td[@class="propertyTJDescription"]//text()')

f = open(zipcode, "a")

for title in description:
	if index < 1:
		together = title + ", " + taxrate[startingNum] + "\n"
		# print(title, taxrate[startingNum])
		f.write(together)
	else:
		startingNum = startingNum + 8
		together = title + ", " + taxrate[startingNum] + "\n"
		f.write(together)
		# print(title, taxrate[startingNum])
	index += 1
f.close()
