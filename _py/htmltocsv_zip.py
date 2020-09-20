from lxml import html
import requests, csv, os, os.path

DIR = '../_propcsv_zipnames/'
ZIPCSV = '../_zipcsv/'
list = os.listdir(DIR)

for zipcode in list:
	index = 0
	startingNum = 2
	# file = open(zipcode, "r")
	with open(DIR + zipcode) as csv_file:
		reader = csv.reader(csv_file, delimiter=',')
		for row in reader:
			if row[0] == 'Property ID':
				continue
			else:
				property_id = row[0]

				page = requests.get('http://bexar.trueautomation.com/clientdb/Property.aspx?cid=110&prop_id=' + property_id)
				table = html.fromstring(page.content)

				#This will create a list of buyers:
				taxrate = table.xpath('//table[@class="tableData"]/tr/td//text()')
				#This will create a list of prices
				description = table.xpath('//tr/td[@class="propertyTJDescription"]//text()')

				f = open(ZIPCSV + zipcode, "a")

				for title in description:
					if index < 1:
						together = title + ", " + taxrate[startingNum] + "\n"
						f.write(together)
					else:
						startingNum += 8
						together = title + ", " + taxrate[startingNum] + "\n"
						f.write(together)
					index += 1

				f.close()
			break

	csv_file.close()
