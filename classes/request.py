from classes.store import Store
from classes.shop import Shop


class Request:
    def __init__(self, text):
        self.text = text.split()
        self.from_ = self.text[4]
        self.to = self.text[6]
        self.amount = self.text[1]
        self.product = self.text[2]
        self.action = self.text[0]

    def text(self):
        return self.text()

    # def validate(self, store: Store, shop: Shop):
    #     if not self.amount.isdigit():
    #         return False
    #     if self.to == 'склад':
    #         if self.product not in shop.get_items() or self.amount > shop.get_items()[self.product]:
    #             return False
    #     if self.to == 'магазин':
    #         if self.product not in store.get_items() or self.amount > store.get_items()[self.product]:
    #             return False
    #     if self.action not in ['Доставить', 'Вернуть']:
    #         return False
    #     if len(self.text) != 7:
    #         return False
    #     return True
    def is_valid(self):
        if len(self.text) == 7:
            return True
        else:
            return False
