"""
Creacion de servicio que extraiga los productos
"""

from typing import Dict, Any
import requests
from bs4 import BeautifulSoup
import json
from fastapi import FastAPI

app = FastAPI()


@app.get("/soriana_products/")
def get_soriana_products(url: str):
    # Make request to the URL with headers to avoid being blocked
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
    response = requests.get(url, headers=headers)

    # Check if website is accessible and extract product data if successful
    if response.status_code != 200:
        raise Exception("Website not accessible")
    else:
        soup = BeautifulSoup(response.content, "html.parser")
        product_data = {"url": url, "products": []}
        products = soup.find_all("div", {"class": "product-item"})
        for product in products:
            product_name = product.find("div", {"class": "product-name"}).text.strip()
            product_price = product.find("div", {"class": "product-price"}).text.strip()
            product_data["products"].append({"name": product_name, "price": product_price})

        # Return product data as JSON
        return json.dumps(product_data, indent=4)
