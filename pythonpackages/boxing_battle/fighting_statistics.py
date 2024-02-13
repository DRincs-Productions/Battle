import time
from typing import Optional
from pythonpackages.boxing_battle.fighting_move import (
    AttackMove,
    DefenseMove,
    FightingMove,
)
from pythonpackages.boxing_battle.fighting_state import FightingState
from pythonpackages.renpy_utility.renpy_custom_log import log_warn
from abc import ABC, abstractmethod
import renpy.exports as renpy


class FightingStatistics(ABC):
    def __init__(
        self,
        health: int,
        stamina: int,
        recovery_percentage_stamina: float,
        idle_image: str,
        damage_imaged: str,
    ):
        self.health = health
        self.stamina = stamina
        self.max_health = health
        self.max_stamina = stamina
        self.recovery_percentage_stamina = recovery_percentage_stamina
        self.idle_image = idle_image
        self.damage_imaged = damage_imaged
        self.is_in_damaged_state = False

        self.current_hit_number = None
        self.current_move = None
        self.stun_date_time = None

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

    @property
    def idle_image(self) -> str:
        """The idle image of the character."""
        return self._idle_image

    @idle_image.setter
    def idle_image(self, value: str):
        self._idle_image = value

    @property
    def damage_imaged(self) -> str:
        """The damage image of the character."""
        return self._damage_imaged

    @damage_imaged.setter
    def damage_imaged(self, value: str):
        self._damage_imaged = value

    @property
    def is_in_damaged_state(self) -> bool:
        return self._is_in_damaged_state

    @is_in_damaged_state.setter
    def is_in_damaged_state(self, value: bool):
        self._is_in_damaged_state = value

    @property
    def current_state(self) -> FightingState:
        """The current state of the character."""
        if self.is_in_damaged_state:
            return FightingState.DAMAGED
        elif isinstance(self.current_move, AttackMove):
            return FightingState.ATTACK
        elif isinstance(self.current_move, DefenseMove):
            return FightingState.DEFENSE
        else:
            return FightingState.IDLE

    @property
    def current_hit_number(self) -> int:
        """The current hit of the character."""
        if self._current_hit_number is None:
            return 0
        return self._current_hit_number

    @current_hit_number.setter
    def current_hit_number(self, value: Optional[int]):
        self._current_hit_number = value

    @property
    def current_move(self) -> Optional[FightingMove]:
        """The current move of the character."""
        return self._current_move

    @current_move.setter
    def current_move(self, value: Optional[FightingMove]):
        self._current_move = value

    @property
    def stun_date_time(self) -> Optional[float]:
        """The stun time of the character."""
        return self._stun_date_time

    @stun_date_time.setter
    def stun_date_time(self, value: Optional[float]):
        self._stun_date_time = value

    def damage(
        self,
        rival_attack: Optional[FightingMove],
    ):
        """Calculate the damage of the attack."""
        # stamina_damage = rival_attack.stamina_damage - defense.stamina_resistance
        # health_damage = rival_attack.health_damage - defense.health_resistance
        # if stamina_damage < 0:
        #     stamina_damage = 0
        # if health_damage < 0:
        #     health_damage = 0
        # self.stamina -= stamina_damage

        if not isinstance(rival_attack, AttackMove):
            log_warn(
                "The rival attack is not an attack move.", "FightingStatistics.damage"
            )
            return

        renpy.hide(self.image)
        self.health -= rival_attack.health_damage
        if rival_attack.stun_time > 0:
            self.is_in_damaged_state = True
            self.current_move = None
            self.stun_date_time = time.time() + rival_attack.stun_time
        renpy.show(self.image)
        return

    def remove_damage_state(self):
        """Remove the damage state."""
        if self.stun_time_to_wait > 0:
            return
        renpy.hide(self.image)
        if self.current_state == FightingState.DAMAGED:
            self.is_in_damaged_state = False
        renpy.show(self.image)

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
        amt = self.max_stamina * self.recovery_percentage_stamina / 100
        self.stamina += int(amt)
        if self.stamina > self.max_stamina:
            self.stamina = self.max_stamina

    @property
    def image(self) -> str:
        """Return the image of the character."""
        if self.current_move is None:
            if self.current_state == FightingState.DAMAGED:
                return self.damage_imaged
            else:
                return self.idle_image
        elif isinstance(self.current_move, AttackMove):
            # get image by hit number
            size = len(self.current_move.animation_images)
            if size == 0:
                self.current_move.animation_image
            index = self.current_hit_number % size
            return self.current_move.animation_images[index]

        return self.current_move.animation_image

    @property
    def stun_time_to_wait(self) -> float:
        """The stun time to wait. If the value is equal or less than 0, it will return 0."""
        if self.stun_date_time is None:
            return 0
        value = self.stun_date_time - time.time()
        if value > 0:
            return round(value, 2)
        self.stun_date_time = None
        return 0

    @property
    def stun_time_to_wait_into_timer(self) -> float:
        """The stun time to wait. Is equal to stun_time_to_wait, but if the value is equal or less than 0, it will return 0.01."""
        value = self.stun_time_to_wait
        if value <= 0:
            return 0.01
        return value

    @abstractmethod
    def set_move(self, move: Optional[FightingMove]):
        pass
