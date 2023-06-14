from sys import argv
from typing import Protocol


class PokeBalls(Protocol):
    def catch(self) -> bool:
        ...

    def catch_rate(self) -> int:
        ...

    def __repr__(self) -> str:
        ...


class PokeBall:
    def catch(self) -> bool:
        return True

    def catch_rate(self) -> int:
        return 10

    def __repr__(self) -> str:
        return "PokeBall"


class GreatBall:
    def catch(self) -> bool:
        return True

    def catch_rate(self) -> int:
        return 20

    def __repr__(self) -> str:
        return "GreatBall"


class Potions(Protocol):
    def use(self) -> bool:
        ...

    def heal_amount(self) -> int:
        ...

    def __repr__(self) -> str:
        ...


class Potion:
    def use(self) -> bool:
        return True

    def heal_amount(self) -> int:
        return 10

    def __repr__(self) -> str:
        return "Potion"


class SuperPotion:
    def use(self) -> bool:
        return True

    def heal_amount(self) -> int:
        return 20

    def __repr__(self) -> str:
        return "SuperPotion"


class PokeItemFactory(Protocol):
    def create_pokeball(self) -> PokeBalls:
        ...

    def create_potion(self) -> Potions:
        ...


class NormalPokeItemFactory:
    def create_pokeball(self) -> PokeBall:
        return PokeBall()

    def create_potion(self) -> Potion:
        return Potion()


class BetterPokeItemFactory:
    def create_pokeball(self) -> GreatBall:
        return GreatBall()

    def create_potion(self) -> SuperPotion:
        return SuperPotion()


def useBall(ball: PokeBalls) -> bool:
    print(f"Using {ball}")
    return ball.catch()


def main():
    item_type = argv[1]

    factory = (
        NormalPokeItemFactory() if item_type == "normal" else BetterPokeItemFactory()
    )

    ball = factory.create_pokeball()
    potion = factory.create_potion()

    print(ball)
    print(useBall(ball))
    print(potion)


if __name__ == "__main__":
    main()
