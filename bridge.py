from typing import Protocol
from dataclasses import dataclass


@dataclass
class Pokemon:
    id: int
    name: str
    height: int
    order: int
    weight: int


@dataclass
class PokemonMove:
    id: int
    name: str
    accuracy: int
    pp: int
    power: int


class PokeAPIClient(Protocol):
    def getPokemon(self, name: str) -> Pokemon:
        ...

    def getMove(self, name: str) -> PokemonMove:
        ...


class PokeDex:
    def __init__(self, apiClient: PokeAPIClient) -> None:
        self.__api_client = apiClient

    def getPokemonInfo(self, name: str) -> Pokemon:
        return self.__api_client.getPokemon(name)

    def getMoveforPokemon(self, move: str, pokemon: Pokemon) -> PokemonMove:
        # do stuff
        move_data = self.__api_client.getMove(move)
        print(f"{pokemon.name}'s move {move_data.name}")
        return PokemonMove(id=1, name="takle", accuracy=80, pp=35, power=35)
