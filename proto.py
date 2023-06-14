from typing import Protocol, List


class PokemonAPI(Protocol):
    def getPokemon(self, name: str) -> str:
        ...

    def getItem(self, name: str) -> str:
        ...

    def getCharacter(self, name: str) -> str:
        ...


class PokeClient:
    def getPokemon(self, name: str) -> str:
        return "Pikachu"

    def getItem(self, name: str) -> str:
        return "Pokeball"

    def getCharacter(self, name: str) -> str:
        return "Ash"


def getStarters(gen: int, client: PokemonAPI) -> List[str]:
    pokemon = client.getCharacter("pikachu")
    return [pokemon]


def main() -> None:
    client = PokeClient()
    print(type(client))
    starters = getStarters(1, client)
    print(starters)


if __name__ == "__main__":
    main()
