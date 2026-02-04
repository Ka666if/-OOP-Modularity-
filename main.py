from models import Product
from cart import ShoppingCart


def main():
    laptop = Product("Ноутбук", 90000, 3)
    phone = Product("Смартфон", 60000, 2)
    headphones = Product("Наушники", 8000, 1)

    cart = ShoppingCart()
    cart.add_item(laptop)
    cart.add_item(phone)
    cart.add_item(headphones)

    print("Итоговый чек:")
    for item in cart.items:
        print(f"- {item.name}: {item.price} руб.")

    print(f"Итого: {cart.get_total()} руб.")


if __name__ == "__main__":
    main()
