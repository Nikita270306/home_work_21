from classes.store import Store
from classes.shop import Shop
from classes.request import Request


def main():
    store = Store(items={
            "яблоки": 10,
            "бананы": 17,
            "киви": 14,
            "груши": 9
        }
    )
    shop = Shop(items={
            "яблоки": 3,
            "торты": 2,
            "манго": 1,
            "игрушки": 5
        }
    )
    print("Приветствую! Здесь вы можете заказать товар!")
    print('сейчас хранится:')
    print('в магазине хранится:')
    shop.get_information()
    print('на складе хранится:')
    store.get_information()
    while True:
        print("Заказ должен выглядеть так:\nДоставить 3 печеньки из склад в магазин")
        user_input = input().lower()
        if user_input == 'домой':
            print('End')
            break
        try:
            request_ = Request(user_input)
        except IndexError:
            print('ваш запрос не соответствует запросу из примера')
        if request_.is_valid():
            if request_.text[0].lower() == "доставить":
                try:
                    count = int(request_.amount)
                except ValueError:
                    print("вы не ввели количество товара, попробуйте снова!)")
                if request_.from_.lower() != "склад":
                    print("Вы не ввели откуда доставить товар, попробуйте снова")
                    continue

                if request_.to.lower() != "магазин":
                    print("Вы не ввели куда доставить товар, попробуйте снова")
                    continue
                try:
                    store.remove(request_.product, count)
                except Exception:
                    continue
                try:
                    shop.add(request_.product, count)
                except Exception:
                    continue
            else:
                print("Вы ввели запрос не так как в примере!")
            print("В складе хранится:")
            store.get_information()

            print("В магазине хранится:")
            shop.get_information()

if __name__ == '__main__':
    main()
