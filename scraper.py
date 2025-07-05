import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_laptops():
    url = "http://webscraper.io/test-sites/e-commerce/static/computers/laptops"
    resp = requests.get(url)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    products = []
    for card in soup.select(".thumbnail"):
        title = card.select_one(".title")["title"]
        desc = card.select_one(".description").text.strip()
        price = card.select_one(".price").text.strip()
        rating = len(card.select(".ratings p.rated"))
        img = card.select_one("img")["src"]
        img_url = f"http://webscraper.io{img}"

        products.append({
            "Title": title,
            "Description": desc,
            "Price": price,
            "Rating": rating,
            "Image": img_url
        })

    df = pd.DataFrame(products)
    df.to_excel("products.xlsx", index=False)
    return products

if __name__ == "__main__":
    items = scrape_laptops()
    print(f"Scraped {len(items)} products!")

