"""
El siguiente script en Python utiliza BeautifulSoup para extraer el menú del sitio web de Soriana 
y guardar la información en un archivo JSON.
"""

import requests
from bs4 import BeautifulSoup
import json

def get_menu(url):
    # Make request to the URL with headers to avoid being blocked
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Error: {response.status_code}")
    soup = BeautifulSoup(response.content, 'html.parser')
    menu = []
    for li in soup.select("#level1 > ul > li"):
        department = li.select_one("h2").text.strip()
        department_url = li.select_one("a").get("href")
        department_menu = {
            "department": department,
            "url": department_url,
            "categories": []
        }
        #Iteramos sobre el menu y departamentos
        for sub_menu in li.select(".category"):
            category = sub_menu.select_one(".label").text.strip()
            category_url = sub_menu.select_one("a").get("href")
            subcategories = []
            for subcategory in sub_menu.select(".subcategory > a"):
                subcategory_name = subcategory.text.strip()
                subcategory_url = subcategory.get("href")
                subcategories.append({
                    "name": subcategory_name,
                    "url": subcategory_url
                })
            department_menu["categories"].append({
                "name": category,
                "url": category_url,
                "subcategories": subcategories
            })
        menu.append(department_menu)
    with open("soriana_menu.json", "w") as f:
        json.dump(menu, f)

if __name__ == "__main__":
    url = "https://www.soriana.com/"
    get_menu(url)

