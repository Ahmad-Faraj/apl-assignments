import requests
from bs4 import BeautifulSoup
import json
def scrape_local():
with open("sample_data.html", "r", encoding="utf-8") as f:
soup = BeautifulSoup(f.read(), "html.parser")
data = []
for product in soup.find_all("div", class_="product"):
{
class_="name").get_text(),
class_="price").get_text(),
class_="description").get_text(),
}
)
def scrape_web():
response = requests.get("http://quotes.toscrape.com/",
timeout=5)
soup = BeautifulSoup(response.content, "html.parser")
data = []
for quote in soup.find_all("div", class_="quote"):
{
class_="text").get_text(),
class_="author").get_text(),
}
)
if __name__ == "__main__":
try:
data = scrape_web()
print(f"Web: {len(data)} items")
except:
data = scrape_local()
print(f"Local: {len(data)} items")
with open("scraped_data.json", "w", encoding="utf-8") as f:
json.dump(data, f, indent=2, ensure_ascii=False)
print("Saved")