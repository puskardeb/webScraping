import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

uClient = uReq('https://www.newegg.com/global/in/Product/ProductList.aspx?Submit=ENE&N=-1&IsNodeId=1&Description=mechanical%20keyboard&bop=And&Order=PRICE&PageSize=36')
page_html=uClient.read()
uClient.close()

pageSoup=soup(page_html,"html.parser")

containers = pageSoup.findAll('div',class_='item-container')

filename = 'mechanicalKeyboards.csv'
f = open(filename, 'w')

headers = 'Product Name,Price\n'
f.write(headers)

for i in containers:
	
	titleContainer = i.findAll('a',class_ = 'item-title')
	productName = titleContainer[0].text
	priceContainer = i.findAll('li',class_='price-current')
	price = priceContainer[0].text.split()
	

	
	print('productName ' + productName)
	print('price Rs' + price[1] + "\n\n\n")

	f.write(productName.replace(',','|') + ',' + price[1].replace(',','') + '\n')

