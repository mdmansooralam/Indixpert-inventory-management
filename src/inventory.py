
import json
import os
from src.product import Product

INVENTORY_FILE = 'inventory.json'

class Inventory:
    def __init__(self):
        self.products = self.load_inventory()

    def load_inventory(self):
        """Load Products from json file"""
        if os.path.exists(INVENTORY_FILE):
            with open(INVENTORY_FILE, 'r') as file:
                inventory_products = json.load(file)
                return [Product(**pd) for pd in inventory_products]
        else:
            return []

    def save_inventory(self):
        with open(INVENTORY_FILE, 'w') as file:
            inventory_products = [product.__dict__ for product in self.products]
            json.dump(inventory_products, file, indent=4)