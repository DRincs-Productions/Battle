from typing import Optional
from pythonpackages.boxing_battle.fighting_move import (
    AttackMove,
    DefenseMove,
    FightingMove,
)


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


class PlayerStatistics(FightingStatistics):
    def __init__(
        self,
        health: int,
        stamina: int,
        recovery_percentage_stamina: float,
        x_button: Optional[FightingMove] = None,
        y_button: Optional[FightingMove] = None,
        a_button: Optional[FightingMove] = None,
        b_button: Optional[FightingMove] = None,
        up_button: Optional[FightingMove] = None,
        down_button: Optional[FightingMove] = None,
        left_button: Optional[FightingMove] = None,
        right_button: Optional[FightingMove] = None,
    ):
        super().__init__(
            health,
            stamina,
            recovery_percentage_stamina,
        )
        self.x_button = x_button
        self.y_button = y_button
        self.a_button = a_button
        self.b_button = b_button
        self.up_button = up_button
        self.down_button = down_button
        self.left_button = left_button
        self.right_button = right_button

        self.x_enabled = True
        self.y_enabled = True
        self.a_enabled = True
        self.b_enabled = True
        self.up_enabled = True
        self.down_enabled = True
        self.left_enabled = True
        self.right_enabled = True

    @property
    def x_button(self) -> Optional[FightingMove]:
        """The x button move."""
        return self._x_button

    @x_button.setter
    def x_button(self, value: Optional[FightingMove]):
        self._x_button = value

    @property
    def y_button(self) -> Optional[FightingMove]:
        """The y button move."""
        return self._y_button

    @y_button.setter
    def y_button(self, value: Optional[FightingMove]):
        self._y_button = value

    @property
    def a_button(self) -> Optional[FightingMove]:
        """The a button move."""
        return self._a_button

    @a_button.setter
    def a_button(self, value: Optional[FightingMove]):
        self._a_button = value

    @property
    def b_button(self) -> Optional[FightingMove]:
        """The b button move."""
        return self._b_button

    @b_button.setter
    def b_button(self, value: Optional[FightingMove]):
        self._b_button = value

    @property
    def up_button(self) -> Optional[FightingMove]:
        """The up button move."""
        return self._up_button

    @up_button.setter
    def up_button(self, value: Optional[FightingMove]):
        self._up_button = value

    @property
    def down_button(self) -> Optional[FightingMove]:
        """The down button move."""
        return self._down_button

    @down_button.setter
    def down_button(self, value: Optional[FightingMove]):
        self._down_button = value

    @property
    def left_button(self) -> Optional[FightingMove]:
        """The left button move."""
        return self._left_button

    @left_button.setter
    def left_button(self, value: Optional[FightingMove]):
        self._left_button = value

    @property
    def right_button(self) -> Optional[FightingMove]:
        """The right button move."""
        return self._right_button

    @right_button.setter
    def right_button(self, value: Optional[FightingMove]):
        self._right_button = value

    @property
    def x_enabled(self) -> bool:
        """If the x button is enabled."""
        return self._x_enabled

    @x_enabled.setter
    def x_enabled(self, value: bool):
        self._x_enabled = value

    @property
    def y_enabled(self) -> bool:
        """If the y button is enabled."""
        return self._y_enabled

    @y_enabled.setter
    def y_enabled(self, value: bool):
        self._y_enabled = value

    @property
    def a_enabled(self) -> bool:
        """If the a button is enabled."""
        return self._a_enabled

    @a_enabled.setter
    def a_enabled(self, value: bool):
        self._a_enabled = value

    @property
    def b_enabled(self) -> bool:
        """If the b button is enabled."""
        return self._b_enabled

    @b_enabled.setter
    def b_enabled(self, value: bool):
        self._b_enabled = value

    @property
    def up_enabled(self) -> bool:
        """If the up button is enabled."""
        return self._up_enabled

    @up_enabled.setter
    def up_enabled(self, value: bool):
        self._up_enabled = value

    @property
    def down_enabled(self) -> bool:
        """If the down button is enabled."""
        return self._down_enabled

    @down_enabled.setter
    def down_enabled(self, value: bool):
        self._down_enabled = value

    @property
    def left_enabled(self) -> bool:
        """If the left button is enabled."""
        return self._left_enabled

    @left_enabled.setter
    def left_enabled(self, value: bool):
        self._left_enabled = value

    @property
    def right_enabled(self) -> bool:
        """If the right button is enabled."""
        return self._right_enabled

    @right_enabled.setter
    def right_enabled(self, value: bool):
        self._right_enabled = value

    def disable_all_buttons(self):
        """Disable all buttons."""
        self.x_enabled = False
        self.y_enabled = False
        self.a_enabled = False
        self.b_enabled = False
        self.up_enabled = False
        self.down_enabled = False
        self.left_enabled = False
        self.right_enabled = False

    def enable_all_buttons(self):
        """Enable all buttons."""
        self.x_enabled = True
        self.y_enabled = True
        self.a_enabled = True
        self.b_enabled = True
        self.up_enabled = True
        self.down_enabled = True
        self.left_enabled = True
        self.right_enabled = True
