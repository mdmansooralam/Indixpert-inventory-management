import json
import os
from src.product import Product

SALES_FILE = 'sales.json'


class Sales():
    def __init__(self):
        self.all_sales = self.load_sales()

    def load_sales(self):
        """Load Sales record from json file"""
        if os.path.exists(SALES_FILE):
            with open(SALES_FILE, 'r') as file:
                sales_record = json.load(file)
                return [Product(**pd) for pd in sales_record]
        else:
            return []
            
    def save_sales(self):
        """Save Sales Record to json file"""
        with open(SALES_FILE, 'w') as file:
            sales_record = [sales.__dict__ for sales in self.all_sales]
            json.dump(sales_record, file, indent=4)