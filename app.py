from bs4 import BeautifulSoup as bs
from table import html
import json, csv
page = bs(html, features="lxml")
head = page.find('thead')
headings = [item.text for item in head.find_all('th')]
data = []
body = page.find('tbody')
rows = body.find_all('tr') 
for row in rows:
    row_data = []
    row = row.find_all('td')
    for index,data_html in enumerate(row):
        row_data.append(data_html.text) 
    row_data = dict(zip(headings, row_data))
    row_data['link'] = row[0].find('a').attrs['href']
    data.append(row_data)

# StackOverflow (CSV)
keys = data[0].keys()
with open('questions.csv', 'w', newline='')  as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(data)    

# Json 
# json.dump(data)
# with open("questions.json", "w") as fp:
    # json.dump(data,fp) 