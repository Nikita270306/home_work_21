from abc import ABC, abstractmethod


class Storage(ABC):

    @abstractmethod
    def __init__(self, items, capacity):
        self._items: dict[str, int] = items
        self._capacity: int = capacity

    @abstractmethod
    def add(self, title: str, quantity: int) -> None:
        pass

    @abstractmethod
    def remove(self, title: str, quantity: int) -> None:
        pass

    @abstractmethod
    def get_free_space(self) -> int:
        pass

    @abstractmethod
    def get_items(self) -> dict[str, int]:
        pass

    @abstractmethod
    def get_unique_items_count(self) -> int:
        pass
