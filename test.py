"""
Creacion de pruebas... 
"""

import unittest
import json
from scraping import get_menu

class TestMenuExtraction(unittest.TestCase):
    def test_get_menu(self):
        url = "https://www.soriana.com/"
        get_menu(url)
        with open("soriana_menu.json", "r") as f:
            menu = json.load(f)
        self.assertIsInstance(menu, list)
        self.assertGreater(len(menu), 0)
        for department in menu:
            self.assertIsInstance(department["department"], str)
            self.assertIsInstance(department["url"], str)
            self.assertIsInstance(department["categories"], list)
            for category in department["categories"]:
                self.assertIsInstance(category["name"], str)
                self.assertIsInstance(category["url"], str)
                self.assertIsInstance(category["subcategories"], list)
                for subcategory in category["subcategories"]:
                    self.assertIsInstance(subcategory["name"], str)
                    self.assertIsInstance(subcategory["url"], str)

if __name__ == "__main__":
    unittest.main()
