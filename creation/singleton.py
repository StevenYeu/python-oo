from __future__ import annotations
from typing import Dict, Optional


class PokeWorldResources(object):
    __resources: Dict[str, int] = {
        "Potion": 100,
        "Full Restore": 100,
        "Rare Candy": 100,
        "PokeBall": 1000,
        "MasterBall": 1,
    }

    __instance: Optional[PokeWorldResources] = None

    def __new__(cls) -> PokeWorldResources:
        if cls.__instance is None:
            cls.__instance = super(PokeWorldResources, cls).__new__(cls)
        return cls.__instance

    @classmethod
    def getResources(cls, resource: str) -> int:
        return cls.__resources[resource]

    @classmethod
    def takeResource(cls, resource: str) -> None:
        if cls.__resources[resource] > 0:
            cls.__resources[resource] -= 1


def main() -> None:
    appState = PokeWorldResources()
    appState.takeResource("MasterBall")
    appState2 = PokeWorldResources()
    print(appState == appState2)
    print(appState2.getResources("MasterBall"))


if __name__ == "__main__":
    main()
