import requests
from bs4 import BeautifulSoup
import csv
import lxml
import json
from config.settings import BASE_DIR


pgapage = {
    'cfia': 'https://www.cbsa-asfc.gc.ca/prog/sw-gu/regcom-marreg/cfia-acia-eng.html',
    'cnsc': 'https://www.cbsa-asfc.gc.ca/prog/sw-gu/regcom-marreg/cnsc-ccsn-eng.html',
    'eccc': 'https://www.cbsa-asfc.gc.ca/prog/sw-gu/regcom-marreg/eccc-eccc-eng.html',
    'dfo': 'https://www.cbsa-asfc.gc.ca/prog/sw-gu/regcom-marreg/dfo-mpo-eng.html',
    'gac': 'https://www.cbsa-asfc.gc.ca/prog/sw-gu/regcom-marreg/gac-amc-eng.html',
    'hc': 'https://www.cbsa-asfc.gc.ca/prog/sw-gu/regcom-marreg/hc-sc-eng.html',
    'nrcan': 'https://www.cbsa-asfc.gc.ca/prog/sw-gu/regcom-marreg/nrc-rnc-eng.html',
    'phac': 'https://www.cbsa-asfc.gc.ca/prog/sw-gu/regcom-marreg/phac-aspc-eng.html',
    'tc': 'https://www.cbsa-asfc.gc.ca/prog/sw-gu/regcom-marreg/tc-eng.html'
}


def get_table_data(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    data = []

    table = soup.find(class_='brdr-bttm')

    # headers
    table_head = table.find('thead')

    rows = table_head.find_all('tr')
    for row in rows:
        cols = row.find_all('th')
        cols = [' '.join((ele.text.strip()).split()) for ele in cols]
        data.append([ele for ele in cols])

    # body
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')       
        # cols = [ele.text.strip() for ele in cols]
        cols = [' '.join((ele.text.strip()).split()) for ele in cols]
        data.append([ele for ele in cols])

    return data

def get_logic_data(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    data = []

    table = soup.find(class_='table-bordered')

    # headers
    table_head = table.find('thead')

    rows = table_head.find_all('tr')
    for row in rows:
        cols = row.find_all('th')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols])

    # body
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')       
        cols = [ele.text.strip() for ele in cols]       
        data.append([ele for ele in cols])
    return data

def sima_info():
    url = "https://www.cbsa-asfc.gc.ca/sima-lmsi/mif-mev/menu-eng.html"

    html = requests.get(url)
    # print(html.text)
    # print(html)    
    soup = BeautifulSoup(html.text, 'lxml')
    
    data = []

    table = soup.find(class_="wb-tables")

    table_head = table.find('thead')
    rows = table_head.find_all('tr')
    for row in rows:
        cols = row.find_all('th')
        cols = [ele.text.strip() for ele in cols]
        cols = cols + ['link']
        data.append([ele for ele in cols])

    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')

        link = cols[0].find('a').attrs['href']

        cols = [ele.text.strip().replace('\t\t\t', '').replace('.', '') for ele in cols]        
        cols = cols + [link]    
        data.append([ele for ele in cols])
    return data



def data_to_csv(pga, dtype='data'):

    # open csv file
    if dtype == 'data':
        data = get_table_data(pga)
    elif dtype == 'logic':
        data = get_logic_data(pga)
    else:
        raise ValueError("dtype must be 'logic' or 'data'")

    with open(BASE_DIR / f'tarifftank/data/ca/{pga}_PGA_{"LOGIC" if dtype.lower() == "logic" else "DATA"}', 'w') as f:

        writer = csv.writer(f, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_MINIMAL)
        #data = get_table_data(pgapage[pga])

        for line in data:
            writer.writerow(line)


def data_to_json(data, json_filename):
    path = BASE_DIR / f'tarifftank/data/ca/{json_filename}'
    keys = data[0]
    rows = data[1:]

    out = []

    for row in rows:
        out.append({k:v for k, v in zip(keys, row)})

    with open(path, 'w') as json_file:
        json.dump(out, json_file)


