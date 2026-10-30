
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        if product.quantity > 0:
            self.products.append(product)
            product.quantity -= 1
            print("Товар додано!")
        else:
            print("Немає в наявності!")

    def remove_product(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                product.quantity += 1
                print("Товар видалено!")
                return
        print("Товар не знайдено!")

    def total_price(self):
        total = 0
        for product in self.products:
            total += product.price
        return total

    def show_cart(self):
        if len(self.products) == 0:
            print("Кошик порожній!")
        else:
            for product in self.products:
                print(product.name, "-", product.price, "грн")

        print("Загальна ціна:", self.total_price(), "грн")


cart = Cart()
shop = []

while True:
    print("\n1. Додати товар у магазин")
    print("2. Показати товари")
    print("3. Додати товар у кошик")
    print("4. Видалити товар з кошика")
    print("5. Показати кошик")
    print("6. Вийти")

    choice = input("Ваш вибір: ").strip()

    if choice == "1":
        name = input("Назва товару: ")
        price = int(input("Ціна: "))
        quantity = int(input("Наявність: "))

        product = Product(name, price, quantity)
        shop.append(product)
        print("Товар успішно створено!")

    elif choice == "2":
        if len(shop) == 0:
            print("Магазин порожній!")
        else:
            for product in shop:
                print(product.name, "-", product.price,
                      "грн | Наявність:", product.quantity)

    elif choice == "3":
        name = input("Введіть назву товару: ")

        for product in shop:
            if product.name == name:
                cart.add_product(product)
                break
        else:
            print("Товар не знайдено!")

    elif choice == "4":
        name = input("Назва товару: ")
        cart.remove_product(name)

    elif choice == "5":
        cart.show_cart()

    elif choice == "6":
        print("До побачення!")
        break

    else:
        print("Неправильний вибір!")
