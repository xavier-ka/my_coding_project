#Office Supplies Inventory Management System

#This Python project manages an inventory of office supplies, allowing you to track stock levels, add, remove, and update items.

#-Add office supply items with name, quantity, and price
#-Remove items from the inventory
#-Update the quantity of existing items
#-View all items currently in the inventory

import csv
import os

class InventoryItem:
    """Represents an inventory item with a name, quantity, and price."""
    def _init_(self, name, quantity, price):
        self.name = name
        self.price = float(price)

    def _str_(self):
        return f"{self.name}: {self.quantity} units @ ${self.price:.2f}"

class InventoryManager:
    """Manages office supplies inventory using a CSV file.""" 
    def _init_(self, inventory_file="inventory.csv"):
        self.inventory_file = inventory_file
        self.inventory = self.load_inventory()
        
    def load_inventory(self):
        """Loads inventory from CSV file."""
        if os.path.exists(self.inventory_file):
            with open(self.inventory_file, 'r') as file:
                return [InventoryItem(*row) for row in csv.reader(file)]
        return []

    def save_inventory(self):
        """Saves inventory to CSV file."""
        with open(self.inventory_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows([[item.name, item.quantity, item.price] for item in self.inventory])
            
    def add_item(self, name, quantity, price):
        """Adds a new item to the inventory."""
        self.inventory.append(InventoryItem(name, int(quantity), float(price)))
        self.save_inventory()

    def update_item(self, name, quantity=None, price=None):
        """Updates an existing item."""
        for item in self.inventory:
            if item.name == name:
                if quantity: item.quantity = int(quantity)
                if price: item.price = float(price)
                self.save_inventory()
                return
        print(f"{name} not found.")

    def remove_item(self, name):
        """Removes an item from the inventory."""
        self.inventory = [item for item in self.inventory if item.name != name]
        self.save_inventory()

    def view_inventory(self):
        """Displays the current inventory."""
        if self.inventory:
            for item in self.inventory:
                print(item)
                
        else:
            print("Inventory is empty.")

    def total_inventory_value(self):
        """Calculates the total value of the inventory."""
        total_value = sum(item.quantity * item.price for item in self.inventory)
        print(f"Total inventory value: ${total_value:.2f}")

def main():
    manager = InventoryManager()
    options = {
        '1': manager.view_inventory,
        '2': lambda: manager.add_item(input("Item name: "), input("Quantity: "), input("Price: ")),
        '3': lambda: manager.remove_item(input("Item name to remove: ")),
        '4': lambda: manager.update_item(input("Item name: "), input("New quantity (optional): "), input("New price (optional): ")),
        '5': manager.total_inventory_value,
    }
        
    while True:
        print("\n1. View Inventory\n2. Add Item\n3. Remove Item\n4. Update Item\n5. Total Inventory Value\n6. Exit")
        choice = input("Choose an option: ")
        if choice == '6':
            break
        options.get(choice, lambda: print("Invalid choice."))()

if __name__ == "_main_":
    main()
        
        
        
