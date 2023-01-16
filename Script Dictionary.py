import requests
from bs4 import BeautifulSoup
import json
from json_helper import get_unique_numbers, read_words_from_json, write_to_json

array = read_words_from_json()

url = 'https://studynow.ru/dicta/allwords'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

table = soup.find('table', attrs={'id': 'wordlist'})
if table:
    rows = table.find_all('tr')
    for row in rows:
        columns = row.find_all('td')
        column = columns[1]
        new_column = column.text.lower()
        if ' ' in new_column or '-' in new_column or '.' in new_column or ']' in new_column:
            continue
        array.append(new_column)

unique_words = get_unique_numbers(array)
unique_words.sort()

write_to_json(array)
