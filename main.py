from bs4 import BeautifulSoup
import requests

url = "https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
table = soup.find("table", {"class": "table"})
