1. Which Python library is best suited for sending HTTP requests?
7. The compile() function is used in scraping to:
Requests: is a lightweight HTTP library for fetching static HTML content.
Answer:
import requests
from bs4 import BeautifulSoup
url = "https://example.com"
response = requests.get(url)
if response.status_code == 200:
soup = BeautifulSoup(response.text, 'html.parser')
title = soup.title.string if soup.title else "No
print(f"Page Title: {title}")
else:
print(f"Failed to fetch page. Status code:
{response.status_code}")
import requests
from bs4 import BeautifulSoup
url = "https://example.com"
response = requests.get(url)
if response.status_code == 200:
soup = BeautifulSoup(response.text, 'html.parser')
links = soup.find_all('a', href=True)
if links:
for link in links:
href = link['href']
print(href)
else:
print("No links found.")
else:
print(f"Failed to fetch page. Status code:
{response.status_code}")
from bs4 import BeautifulSoup
html = """
soup = BeautifulSoup(html, 'html.parser')
rows = soup.find_all('tr')
for row in rows:
cells = [cell.get_text(strip=True) for cell in
print(cells)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
search_box = driver.find_element(By.NAME, "q")
print("Page Title:", driver.title)
from bs4 import BeautifulSoup
import csv
html = """
soup = BeautifulSoup(html, 'html.parser')
fruits = [li.get_text(strip=True) for li in
with open('fruits.csv', 'w', newline='', encoding='utf-
8') as csvfile:
writer = csv.writer(csvfile)
for fruit in fruits:
print("Saved to fruits.csv")