import datetime
import requests
from lxml import html

current_datetime = datetime.datetime.now()
formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
url = 'https://www.ilboursa.com/marches/aaz'
response = requests.get(url)
tree = html.fromstring(response.content)

element = tree.xpath('//*[@id="tabQuotes"]/tbody')
List = []
for e in element:
    info = e.text_content().replace(' ', '').replace('\r\n', '+')
    List = [i.split('+') for i in info.split('++')][1:-1]

for item in List[1:]:
    del item[0]

def printfy(table):
	print("Tunisian stock exchange at:", formatted_datetime)
	table = [['Name' , 'Opening', 'High', 'Low', 'Volume(shares)', 'Volume(TND)', 'Last', 'Variation']] + table
	col_width = [max(len(item)+1 for item in col) for col in zip(*table)]
	for line in table:
		print("| ".join(item.ljust(width) for item, width in zip(line, col_width)))
        
printfy(List)

 #nom , ouverture , +Haut , +Bas , Volume(titres) , Volume(DT) , Dernier , Varitation