class SwitchGame:
    def __init__(self, name: str) -> None:
        self.name = f"SwitchGame: {name}"


class Switch:
    def canPlay(self, game: SwitchGame) -> bool:
        return "SwitchGame" in game.name


class ThreeDSGame:
    def __init__(self, name: str) -> None:
        self.name = f"3DS Game: {name}"


class SwitchPort:
    def __init__(self, game: ThreeDSGame) -> None:
        self._threeDSgame = game

    def portGame(self) -> SwitchGame:
        return SwitchGame(self._threeDSgame.name)


def main():
    pokemonX = ThreeDSGame("Pokemon X")
    switch = Switch()
    port = SwitchPort(pokemonX)
    print(switch.canPlay(port.portGame()))


if __name__ == "__main__":
    main()
