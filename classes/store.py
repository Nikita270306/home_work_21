from classes.storage import Storage


class Store(Storage):

    def __init__(self, items, capacity=100):
        super().__init__(items, capacity)

    def add(self, title: str, quantity: int) -> None:
        if 0 < quantity < self._capacity:
            self._items[title] += quantity
            self._capacity -= quantity
            print(f"Курьер везет {quantity} {title} со склада в магазин\n"
                  f"Курьер доставил {quantity} {title} в магазин")
        else:
            print("Недостаточно места на складе")
            raise ValueError

    def remove(self, title: str, quantity: int) -> None:
        if title not in self._items:
            print("На складе нет такого товара")
        if 0 < quantity < self._capacity:
            self._items[title] -= quantity
            self._capacity += quantity
            print('Нужное количество есть в магазине\n'
                  f'Курьер забрал {quantity} {title} с магазина')



    def get_free_space(self) -> int:
        return self._capacity

    def get_items(self) -> dict[str, int]:
        return self._items

    def get_unique_items_count(self) -> int:
        count = 0
        for key, value in self._items.items():
            if self._items[key] > 0:
                count += 1
        return count

    def get_information(self):
        for key, value in self.get_items().items():
            print(f'{key} - {value}')
