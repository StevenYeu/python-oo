from __future__ import annotations

from typing import List


class Pokemon:
    def __init__(self) -> None:
        self._name: str = ""
        self._types: List[str] = []
        self._gender: str = ""
        self._number: int = 0
        self._moves: List[str] = []
        self._locations: List[str] = []

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def type(self) -> List[str]:
        return self._types

    @property
    def gender(self) -> str:
        return self._gender

    @gender.setter
    def gender(self, gender: str) -> None:
        self._gender = gender

    @property
    def number(self) -> int:
        return self._number

    @number.setter
    def number(self, num: int) -> None:
        self._number = num

    @property
    def moves(self) -> List[str]:
        return self._moves

    @property
    def locations(self) -> List[str]:
        return self._locations

    def __repr__(self) -> str:
        return str(self.__dict__)


class PokemonBuilder:
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self.pokemon = Pokemon()

    def setName(self, name: str) -> PokemonBuilder:
        self.pokemon.name = name
        return self

    def addType(self, type: str) -> PokemonBuilder:
        self.pokemon.type.append(type)
        return self

    def setGender(self, gender: str) -> PokemonBuilder:
        self.pokemon.gender = gender
        return self

    def setNumber(self, num: int) -> PokemonBuilder:
        self.pokemon.number = num
        return self

    def addMove(self, move: str) -> PokemonBuilder:
        self.pokemon.moves.append(move)
        return self

    def addLocation(self, location: str) -> PokemonBuilder:
        self.pokemon.locations.append(location)
        return self

    def build(self) -> Pokemon:
        pokemon = self.pokemon
        self.reset()
        return pokemon


def main() -> None:
    builder = PokemonBuilder()

    pokemon: Pokemon = (
        builder.setName("Pikachu")
        .addType("Electric")
        .addMove("Thunder")
        .addMove("ThunderBolt")
        .addMove("Quick Attack")
        .setGender("Male")
        .setNumber(25)
        .addLocation("Pallet Town")
        .build()
    )
    print(pokemon)


if __name__ == "__main__":
    main()
