from lxml import html
import requests, csv, os, os.path

DIR = '../_propcsv_zipnames/'
ZIPCSVDIR = '../_zipcsv/'
ZIPCSV = "zip2propID.csv"
list = os.listdir(DIR)

with open(DIR + ZIPCSV) as csv_file:
	reader = csv.reader(csv_file, delimiter=',')
	for row in reader:
		if row[0] == 'ZIPCode':
			continue
		else:
			zipcode = row[0]
			property_id = row[1]

			print(zipcode + " " + property_id)

			page = requests.get('http://bexar.trueautomation.com/clientdb/Property.aspx?cid=110&prop_id=' + property_id)
			table = html.fromstring(page.content)

			taxrate = table.xpath('//table[@class="tableData"]/tr/td//text()')
			description = table.xpath('//tr/td[@class="propertyTJDescription"]//text()')

			f = open(ZIPCSVDIR + zipcode + ".csv", "a")
			index = 0
			startingNum = 2
			for title in description:
				if index < 1:
					together = title + ", " + taxrate[startingNum].encode('utf-8') + "\n"
					f.write(together)
				else:
					startingNum += 8
					together = title + ", " + taxrate[startingNum].encode('utf-8') + "\n"
					f.write(together)
				index += 1

			f.close()

csv_file.close()
