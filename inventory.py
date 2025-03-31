from logger import logger


class Inventory:
    def __init__(self, max_capacity):
        self.__max_capacity = max_capacity
        self.items = {}
        self.item_count = 0

    def add_item(self, name, price, quantity):
        if name in self.items:
            logger.info(f"Item with name '{name}' already exists")
            return False

        if self.item_count + quantity > self.__max_capacity:
            logger.info("Max capacity reached. Please delete something from the inventory")
            return False
        self.items[name] = {'name': name, 'price': price, 'quantity': quantity}
        self.item_count += quantity
        logger.info(f"Item with name '{name}' added to inventory successfully.")
        return True

    def delete_item(self, name):
        if name not in self.items:
            logger.info(f"Item with name '{name}' does not exist")
            return False
        self.item_count -= self.items[name]['quantity']
        del self.items[name]
        logger.info(f"Item with name '{name}' deleted successfully.")
        return True

    def get_items_in_price_range(self, min_price, max_price):
        results = []
        for item_name in self.items.keys():
            if min_price <= self.items[item_name]['price'] <= max_price:
                logger.info(f"Item with name '{item_name}' is within price range")
                results.append(item_name)
        return results

    def get_most_stocked_item(self):
        max_quantity = 0
        max_quantity_name = None
        for item in self.items.values():
            temp_quantity = item['quantity']
            temp_quantity_name = item['name']
            if temp_quantity > max_quantity:
                max_quantity = temp_quantity
                max_quantity_name = temp_quantity_name
                logger.info(f"Most stocked item with name '{temp_quantity_name}' updated")
        return max_quantity_name


if __name__ == '__main__':
    inventory = Inventory(5)
    inventory.add_item("Chocolate", 4.99, 2)
    inventory.add_item("Cereal", 6.99, 1)
    inventory.add_item("Milk", 3.99, 1)
    inventory.add_item('Butter', 2.99, 1)
    inventory.add_item('Butter', 4.99, 1)
    inventory.add_item('Bread', 4.99, 2)
    print(inventory.delete_item('Bread'))
    print(inventory.get_items_in_price_range(4.50, 6.50))
