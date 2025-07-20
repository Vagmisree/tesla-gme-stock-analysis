import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"
html_data = requests.get(url).text
soup = BeautifulSoup(html_data, "html.parser")

tables = soup.find_all("table")
for table in tables:
    if "GameStop Quarterly Revenue" in str(table):
        df = pd.read_html(str(table))[0]
        break

gme_revenue = df
gme_revenue.columns = ['Date', 'Revenue']
gme_revenue = gme_revenue[gme_revenue['Revenue'] != '']
gme_revenue['Revenue'] = gme_revenue['Revenue'].str.replace(r'\$', '').str.replace(',', '')
gme_revenue['Revenue'] = pd.to_numeric(gme_revenue['Revenue'])

# Display last 5 rows
gme_revenue.tail()
