from classes.store import Store


class Shop(Store):

    def __init__(self, items, capacity=20):
        super().__init__(items, capacity)

    def add(self, title: str, quantity: int) -> None:
        if self.get_unique_items_count() == 5:
            print("В магазине недостаточно места, попробуйте заказать меньше товара")
            raise ValueError
        if 0 < quantity < self._capacity:
           self._items[title] += quantity
           self._capacity -= quantity
           print(f"Курьер везет {quantity} {title} со склада в магазин\n"
                 f"Курьер доставил {quantity} {title} в магазин")

    def remove(self, title: str, quantity: int) -> None:
        if title not in self._items:
            print("На складе нет такого товара")
        if 0 < quantity < self._capacity:
            self._items[title] -= quantity
            self._capacity += quantity
            print('Нужное количество есть в магазине\n'
                  f'Курьер забрал {quantity} {title} с магазина')