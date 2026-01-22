import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website URL (safe practice site)
url = "http://books.toscrape.com/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

titles = []
prices = []

for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    titles.append(title)
    prices.append(price)

# Create DataFrame
df = pd.DataFrame({
    "Book Title": titles,
    "Price": prices
})

# Save to CSV
df.to_csv("books_data.csv", index=False)

print("Web Scraping Completed!")
print(df.head())




