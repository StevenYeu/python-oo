from abc import ABC, abstractmethod
import uuid


class PokeItem(ABC):
    count: int = 0

    def __init__(self, item_type: str, cost: int) -> None:
        super().__init__()
        self.key: str = "TEST"
        self._item_type = item_type
        self.cost = cost
        self.__id = str(uuid.uuid4().bytes)
        PokeItem.count += 1

    @property
    def item_type(self) -> str:
        return self._item_type

    @abstractmethod
    def get_rarity(self) -> int:
        pass


class GreatBall(PokeItem):
    _catch_rate: int = 175

    def __init__(self, item_type: str, cost: int) -> None:
        super().__init__(item_type, cost)

    @property
    def catch_rate(self) -> int:
        return self._catch_rate

    def get_rarity(self) -> int:
        return self.catch_rate


if __name__ == "__main__":
    ball = GreatBall(item_type="great_ball", cost=400)
    print(ball.item_type)
    print(ball.catch_rate)
    print(PokeItem.count)
    print(ball.get_rarity())
