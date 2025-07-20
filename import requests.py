import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
html_data = requests.get(url).text
soup = BeautifulSoup(html_data, "html.parser")

tables = soup.find_all("table")
for table in tables:
    if "Tesla Quarterly Revenue" in str(table):
        df = pd.read_html(str(table))[0]
        break

tesla_revenue = df
tesla_revenue.columns = ['Date', 'Revenue']
tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != '']
tesla_revenue['Revenue'] = tesla_revenue['Revenue'].str.replace(r'\$', '').str.replace(',', '')
tesla_revenue['Revenue'] = pd.to_numeric(tesla_revenue['Revenue'])

# Display last 5 rows
tesla_revenue.tail()
