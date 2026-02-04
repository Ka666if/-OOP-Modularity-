class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        if product.is_available():
            self.items.append(product)
            product.quantity -= 1
        else:
            print(f"Товар {product.name} отсутствует на складе")

    def remove_item(self, product):
        if product in self.items:
            self.items.remove(product)
            product.quantity += 1

    def get_total(self) -> float:
        return sum(item.price for item in self.items)


