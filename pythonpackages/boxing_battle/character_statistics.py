from pythonpackages.boxing_battle.fighting_move import AttackMove, DefenseMove


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

    def dannage(
        self,
        rival_attack: AttackMove,
        defense: DefenseMove,
    ):
        """Calculate the damage of the attack."""
        stamina_damage = rival_attack.stamina_damage - defense.stamina_resistance
        health_damage = rival_attack.health_damage - defense.health_resistance
        if stamina_damage < 0:
            stamina_damage = 0
        if health_damage < 0:
            health_damage = 0

        self.health -= health_damage
        self.strength -= stamina_damage
