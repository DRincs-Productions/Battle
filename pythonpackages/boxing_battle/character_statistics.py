from pythonpackages.boxing_battle.fighting_move import AttackMove, DefenseMove


class FightingStatistics:
    def __init__(
        self,
        health: int,
        stamina: int,
        recovery_percentage_stamina: float,
    ):
        self.health = health
        self.stamina = stamina
        self.max_health = health
        self.max_stamina = stamina
        self.recovery_percentage_stamina = recovery_percentage_stamina

    @property
    def health(self) -> int:
        """The health of the character."""
        return self._health

    @health.setter
    def health(self, value: int):
        self._health = value

    @property
    def max_health(self) -> int:
        """The max health of the character."""
        return self._max_health

    @max_health.setter
    def max_health(self, value: int):
        self._max_health = value

    @property
    def stamina(self) -> int:
        """The stamina of the character."""
        return self._stamina

    @stamina.setter
    def stamina(self, value: int):
        self._stamina = value

    @property
    def max_stamina(self) -> int:
        """The max stamina of the character."""
        return self._max_stamina

    @max_stamina.setter
    def max_stamina(self, value: int):
        self._max_stamina = value

    @property
    def recovery_percentage_stamina(self) -> float:
        """The recovery percentage of the stamina."""
        return self._recovery_percentage_stamina

    @recovery_percentage_stamina.setter
    def recovery_percentage_stamina(self, value: float):
        self._recovery_percentage_stamina = value

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
        self.stamina -= stamina_damage

    @property
    def is_dead(self) -> bool:
        """If the character is dead."""
        return self.health <= 0

    @property
    def is_stamina_empty(self) -> bool:
        """If the stamina is empty."""
        return self.stamina <= 0

    def recover_stamina(self):
        """Recover the stamina."""
        amt = self.stamina * self.recovery_percentage_stamina / 100
        self.stamina += int(amt)
        if self.stamina > self.max_stamina:
            self.stamina = self.max_stamina
