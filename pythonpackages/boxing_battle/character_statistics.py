class FightingStatistics:
    def __init__(
        self,
        health: int,
        strength: int,
    ):
        self.health = health
        self.strength = strength

    @property
    def health(self) -> int:
        """The health of the character."""
        return self._health

    @health.setter
    def health(self, value: int):
        self._health = value

    @property
    def strength(self) -> int:
        """The strength of the character."""
        return self._strength

    @strength.setter
    def strength(self, value: int):
        self._strength = value
