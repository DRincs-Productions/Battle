import random
import time
from typing import Optional, Union
from pythonpackages.boxing_battle.fighting_move import (
    AttackMove,
    DefenseMove,
    DodgeMove,
    FightingMove,
)
from pythonpackages.boxing_battle.fighting_state import FightingState
from pythonpackages.renpy_utility.renpy_custom_log import log_info, log_warn
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
        """The current hit of the opponent."""
        if self._current_hit_number is None:
            return 0
        return self._current_hit_number

    @current_hit_number.setter
    def current_hit_number(self, value: Optional[int]):
        self._current_hit_number = value

    @property
    def current_move(self) -> Optional[FightingMove]:
        """The current move of the opponent."""
        return self._current_move

    @current_move.setter
    def current_move(self, value: Optional[FightingMove]):
        self._current_move = value

    @property
    def stun_date_time(self) -> Optional[float]:
        """The stun time of the opponent."""
        return self._stun_date_time

    @stun_date_time.setter
    def stun_date_time(self, value: Optional[float]):
        self._stun_date_time = value

    def damage(
        self,
        rival_attack: FightingMove,
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

        log_info(f"STUN DATA damage(): {self.stun_date_time}")
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
            log_info("REMOVE DAMAGE STATE")
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
        log_info(f"RECOVER STAMINA: {amt}")
        if self.stamina > self.max_stamina:
            self.stamina = self.max_stamina

    @property
    def image(self) -> str:
        """Return the image of the opponent."""
        log_info(f"STATE: {self.current_state}")
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
        """The stun time to wait."""
        if self.stun_date_time is None:
            return 0
        value = self.stun_date_time - time.time()
        if value > 0:
            return round(value, 2)
        self.stun_date_time = None
        return 0

    @abstractmethod
    def set_move(self, move: Optional[FightingMove]):
        pass


class PlayerStatistics(FightingStatistics):
    def __init__(
        self,
        health: int,
        stamina: int,
        recovery_percentage_stamina: float,
        idle_image: str,
        damage_imaged: str,
        x_button: Optional[FightingMove] = None,
        y_button: Optional[FightingMove] = None,
        a_button: Optional[FightingMove] = None,
        b_button: Optional[FightingMove] = None,
        up_button: Optional[FightingMove] = None,
        down_button: Optional[FightingMove] = None,
        left_button: Optional[FightingMove] = None,
        right_button: Optional[FightingMove] = None,
        time_to_wait_between_hits: float = 0.5,
    ):
        super().__init__(
            health,
            stamina,
            recovery_percentage_stamina,
            idle_image,
            damage_imaged,
        )
        self.x_button = x_button
        self.y_button = y_button
        self.a_button = a_button
        self.b_button = b_button
        self.up_button = up_button
        self.down_button = down_button
        self.left_button = left_button
        self.right_button = right_button
        self.time_to_wait_between_hits = time_to_wait_between_hits

        self.x_enabled = True
        self.y_enabled = True
        self.a_enabled = True
        self.b_enabled = True
        self.up_enabled = True
        self.down_enabled = True
        self.left_enabled = True
        self.right_enabled = True

        self.last_hit_number = 0

    def check_if_button_is_selected(self, button: FightingMove) -> bool:
        """Check if the button is selected."""
        if (
            self.current_move
            and button
            and self.current_move == button
            and self.current_move.selected
        ):
            return self.current_move.selected
        else:
            return False

    @property
    def x_button(self) -> Optional[FightingMove]:
        """The x button move."""
        if self._x_button:
            self._x_button.selected = self.check_if_button_is_selected(self._x_button)

        return self._x_button

    @x_button.setter
    def x_button(self, value: Optional[FightingMove]):
        self._x_button = value

    @property
    def y_button(self) -> Optional[FightingMove]:
        """The y button move."""
        if self._y_button:
            self._y_button.selected = self.check_if_button_is_selected(self._y_button)

        return self._y_button

    @y_button.setter
    def y_button(self, value: Optional[FightingMove]):
        self._y_button = value

    @property
    def a_button(self) -> Optional[FightingMove]:
        """The a button move."""
        if self._a_button:
            self._a_button.selected = self.check_if_button_is_selected(self._a_button)

        return self._a_button

    @a_button.setter
    def a_button(self, value: Optional[FightingMove]):
        self._a_button = value

    @property
    def b_button(self) -> Optional[FightingMove]:
        """The b button move."""
        if self._b_button:
            self._b_button.selected = self.check_if_button_is_selected(self._b_button)

        return self._b_button

    @b_button.setter
    def b_button(self, value: Optional[FightingMove]):
        self._b_button = value

    @property
    def up_button(self) -> Optional[FightingMove]:
        """The up button move."""
        if self._up_button:
            self._up_button.selected = self.check_if_button_is_selected(self._up_button)

        return self._up_button

    @up_button.setter
    def up_button(self, value: Optional[FightingMove]):
        self._up_button = value

    @property
    def down_button(self) -> Optional[FightingMove]:
        """The down button move."""
        if self._down_button:
            self._down_button.selected = self.check_if_button_is_selected(
                self._down_button
            )

        return self._down_button

    @down_button.setter
    def down_button(self, value: Optional[FightingMove]):
        self._down_button = value

    @property
    def left_button(self) -> Optional[FightingMove]:
        """The left button move."""
        if self._left_button:
            self._left_button.selected = self.check_if_button_is_selected(
                self._left_button
            )

        return self._left_button

    @left_button.setter
    def left_button(self, value: Optional[FightingMove]):
        self._left_button = value

    @property
    def right_button(self) -> Optional[FightingMove]:
        """The right button move."""
        if self._right_button:
            self._right_button.selected = self.check_if_button_is_selected(
                self._right_button
            )

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

    @property
    def time_to_wait_between_hits(self) -> float:
        """The time to wait between hits."""
        return self._time_to_wait_between_hits

    @time_to_wait_between_hits.setter
    def time_to_wait_between_hits(self, value: float):
        self._time_to_wait_between_hits = value

    @property
    def last_hit_number(self) -> int:
        """The last hit number."""
        return self._last_hit_number

    @last_hit_number.setter
    def last_hit_number(self, value: int):
        self._last_hit_number = value

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

    def set_move(self, move: Optional[FightingMove]):
        """Set the move of the player."""
        log_info("set_move")
        renpy.hide(self.image)
        log_info(str(move))
        if isinstance(self.current_move, DefenseMove):
            self.current_move.selected = False

        if isinstance(move, DefenseMove):
            log_info("DefenseMove")
            if self.current_move == move:
                self.current_move = None
            else:
                self.current_move = move
                self.current_move.selected = True
        elif isinstance(move, AttackMove):
            self.current_move = move
            self.disable_all_buttons()
            self.last_hit_number += 1
        else:
            self.current_move = move
        renpy.show(self.image)

    def after_hit(self):
        """After a hit."""
        self.enable_all_buttons()
        if isinstance(self.current_move, AttackMove):
            self.current_move = None
            self.is_in_damaged_state = False


class OpponentStatistics(FightingStatistics):
    def __init__(
        self,
        health: int,
        stamina: int,
        recovery_percentage_stamina: float,
        idle_image: str,
        damage_imaged: str,
        defense: Union[list[DefenseMove], DefenseMove] = [],
        attack: Union[list[AttackMove], AttackMove] = [],
        dodge: Union[list[DodgeMove], DodgeMove] = [],
        defensive_percentage: float = 30,
        aggression_percentage: float = 30,
        minimal_repeated_hits: int = 3,
        maximal_repeated_hits: int = 5,
        minimal_time_between_hits: float = 0.2,
        maximal_time_between_hits: float = 0.5,
        dodge_probability: float = 30,
        backlash_probability: float = 30,
        maximum_thinking_time: float = 4,
        minimal_thinking_time: float = 1,
    ):
        super().__init__(
            health,
            stamina,
            recovery_percentage_stamina,
            idle_image,
            damage_imaged,
        )
        if isinstance(defense, DefenseMove):
            defense = [defense]
        self.defense_list = defense
        if isinstance(attack, AttackMove):
            attack = [attack]
        self.attack_list = attack
        if isinstance(dodge, DodgeMove):
            dodge = [dodge]
        self.dodge_list = dodge
        self.defensive_percentage = defensive_percentage
        self.aggression_percentage = aggression_percentage
        self.minimal_repeated_hits = minimal_repeated_hits
        self.maximal_repeated_hits = maximal_repeated_hits
        self.minimal_time_between_hits = minimal_time_between_hits
        self.maximal_time_between_hits = maximal_time_between_hits
        self.dodge_probability = dodge_probability
        self.backlash_probability = backlash_probability
        self.maximum_thinking_time = maximum_thinking_time
        self.minimal_thinking_time = minimal_thinking_time

    @property
    def defense_list(self) -> list[DefenseMove]:
        """The defense list of the opponent."""
        return self._defense_list

    @defense_list.setter
    def defense_list(self, value: list[DefenseMove]):
        self._defense_list = value

    @property
    def random_defense(self) -> Optional[DefenseMove]:
        """Return a random defense move."""
        if len(self.defense_list) == 0:
            return None
        return random.choice(self.defense_list)

    @property
    def attack_list(self) -> list[AttackMove]:
        """The attack list of the opponent."""
        return self._attack_list

    @attack_list.setter
    def attack_list(self, value: list[AttackMove]):
        self._attack_list = value

    @property
    def random_attack(self) -> Optional[AttackMove]:
        """Return a random attack move."""
        if len(self.attack_list) == 0:
            return None
        return random.choice(self.attack_list)

    @property
    def dodge_list(self) -> list[DodgeMove]:
        """The dodge list of the opponent."""
        return self._dodge_list

    @dodge_list.setter
    def dodge_list(self, value: list[DodgeMove]):
        self._dodge_list = value

    @property
    def defensive_percentage(self) -> float:
        """The state time defense percentage of the opponent."""
        return self._defensive_percentage

    @defensive_percentage.setter
    def defensive_percentage(self, value: float):
        self._defensive_percentage = value

    @property
    def aggression_percentage(self) -> float:
        """The aggression percentage of the opponent."""
        return self._aggression_percentage

    @aggression_percentage.setter
    def aggression_percentage(self, value: float):
        self._aggression_percentage = value

    @property
    def minimal_repeated_hits(self) -> int:
        """The minimal repeated hits of the opponent."""
        return self._minimal_repeated_hits

    @minimal_repeated_hits.setter
    def minimal_repeated_hits(self, value: int):
        self._minimal_repeated_hits = value

    @property
    def maximal_repeated_hits(self) -> int:
        """The maximal repeated hits of the opponent."""
        return self._maximal_repeated_hits

    @maximal_repeated_hits.setter
    def maximal_repeated_hits(self, value: int):
        self._maximal_repeated_hits = value

    @property
    def random_repeated_hits(self) -> int:
        """Return a random repeated hits."""
        return random.randint(
            self.minimal_repeated_hits,
            self.maximal_repeated_hits,
        )

    @property
    def minimal_time_between_hits(self) -> float:
        """The minimal time between hits of the opponent."""
        return self._minimal_time_between_hits

    @minimal_time_between_hits.setter
    def minimal_time_between_hits(self, value: float):
        self._minimal_time_between_hits = value

    @property
    def maximal_time_between_hits(self) -> float:
        """The maximal time between hits of the opponent."""
        return self._maximal_time_between_hits

    @maximal_time_between_hits.setter
    def maximal_time_between_hits(self, value: float):
        self._maximal_time_between_hits = value

    @property
    def random_time_between_hits(self) -> float:
        """Return a random time between hits."""
        return random.uniform(
            self.minimal_time_between_hits,
            self.maximal_time_between_hits,
        )

    @property
    def dodge_probability(self) -> float:
        """The dodge probability of the opponent."""
        return self._dodge_probability

    @dodge_probability.setter
    def dodge_probability(self, value: float):
        self._dodge_probability = value

    @property
    def backlash_probability(self) -> float:
        """The backlash probability of the opponent."""
        return self._backlash_probability

    @backlash_probability.setter
    def backlash_probability(self, value: float):
        self._backlash_probability = value

    @property
    def maximum_thinking_time(self) -> float:
        """The maximum thinking time of the opponent."""
        return self._maximum_thinking_time

    @maximum_thinking_time.setter
    def maximum_thinking_time(self, value: float):
        self._maximum_thinking_time = value

    @property
    def minimal_thinking_time(self) -> float:
        """The minimal thinking time of the opponent."""
        return self._minimal_thinking_time

    @minimal_thinking_time.setter
    def minimal_thinking_time(self, value: float):
        self._minimal_thinking_time = value

    @property
    def random_thinking_time(self) -> float:
        """Return a random thinking time."""
        return random.uniform(
            self.minimal_thinking_time,
            self.maximum_thinking_time,
        )

    def update_move(self) -> Optional[FightingMove]:
        """Return the move of the opponent."""
        if self.current_state == FightingState.DAMAGED:
            self.set_move(self.random_defense)
            return self.current_move
        if self.current_state == FightingState.ATTACK:
            return self.current_move
        # random attack
        if random.randint(0, 100) < self.aggression_percentage:
            move = self.random_attack
            if move is not None and self.stamina >= move.stamina_damage:
                log_info("ATTACK")
                self.current_hit_number = 1
                self.stamina -= move.stamina_damage
                self.set_move(move)
                return self.current_move
        # random defanse
        if random.randint(0, 100) < self.defensive_percentage:
            log_info("DEFENSE")
            move = self.random_defense
            if move is not None:
                self.set_move(move)
                return self.current_move
        log_info("IDLE")
        self.set_move(None)
        return self.current_move

    def set_move(self, move: Optional[FightingMove]):
        """Set the move of the opponent."""
        renpy.hide(self.image)
        if isinstance(move, DefenseMove):
            self.current_move = move
        elif isinstance(move, AttackMove):
            self.current_move = move
        else:
            self.current_move = move
        renpy.show(self.image)

    def add_hit(self):
        """Add a hit to the opponent."""
        log_info("HIT: " + str(self.current_hit_number))
        if not isinstance(self.current_move, AttackMove):
            log_warn(
                "The current move is not an attack move.", "OpponentStatistics.add_hit"
            )
            return
        renpy.hide(self.image)
        if (
            self.stamina >= self.current_move.stamina_damage
            and self.current_hit_number <= self.random_repeated_hits
        ):
            self.stamina -= self.current_move.stamina_damage
            self.current_hit_number += 1
        else:
            self.current_hit_number = 0
            self.current_move = self.random_defense
        renpy.show(self.image)
