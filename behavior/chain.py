from __future__ import annotations
from abc import abstractmethod
from typing import Dict, Optional, Protocol


class Handler(Protocol):
    def setNext(self, handler: Handler):
        ...

    @abstractmethod
    def handle(self, req: Dict[str, str]) -> bool:
        raise NotImplementedError


class BaseHandler(Handler):
    def __init__(self) -> None:
        self.next: Optional[Handler] = None

    def setNext(self, handler: Handler):
        self.next = handler

    @abstractmethod
    def handle(self, req: Dict[str, str]) -> bool:
        pass


class CheckPlayer(BaseHandler):
    def __init__(self) -> None:
        super().__init__()

    def handle(self, req: Dict[str, str]) -> bool:
        if "p_one" in req and "p_two" in req:
            one = req["p_one"]
            two = req["p_two"]
            print(f"{one} and {two} are present")

            if self.next:
                return self.next.handle(req)
            else:
                return True
        else:
            print("A player is missing")
            return False


class CheckPokemon(BaseHandler):
    def __init__(self) -> None:
        super().__init__()

    def handle(self, req: Dict[str, str]) -> bool:
        if "pokemon_one" in req and "pokemon_two" in req:
            one = req["pokemon_one"]
            two = req["pokemon_two"]
            print(f"{one} and {two} are present")
            if self.next:
                return self.next.handle(req)
            else:
                return True
        else:
            print("A pokemon is missing")
            return False


def tradeMessage(canTrade: bool) -> str:
    return "Trade is Valid" if canTrade else "Trade is not Valid"


def main():
    handler = CheckPlayer()
    handler.setNext(CheckPokemon())
    request = {
        "p_one": "Ash",
        "p_two": "Gary",
        "pokemon_one": "Pikachu",
        "pokemon_two": "Eevee",
    }

    request_bad = {
        "p_one": "Ash",
        "p_two": "Gary",
        "pokemon_one": "Pikachu",
    }

    print(tradeMessage(handler.handle(request)))
    print(tradeMessage(handler.handle(request_bad)))


if __name__ == "__main__":
    main()
