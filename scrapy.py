
from bs4 import BeautifulSoup
import requests
import jsons

# from google.colab import files

Website_URL = "https://www.pararius.com/apartments/amsterdam"

page = requests.get(Website_URL)  # Throw the response

# print(page)  # printing Response

soup = BeautifulSoup(page.text, "html.parser")  # Throw The page Source

lists = soup.find_all(
  "section", class_=["listing-search-item",
                     "listing-search-item--list"])  # selected multiple class

records = []

for (i, list) in enumerate(lists):
  title = list.find("a",
                    class_="listing-search-item__link--title").text.strip()
  address = list.find("div",
                      class_="listing-search-item__sub-title").text.strip()
  price = list.find("div", class_="listing-search-item__price").text.strip()
  roomsize = list.find(
    "div",
    class_="listing-search-item__features").text.strip().replace('\n', ' || ')

  records.append({
    'id': i,
    "title": title,
    "address": address,
    "price": price,
    "roomsize": roomsize
  })

dicts = jsons.dump(records, indent=2)

print(*dicts, sep=", ")

