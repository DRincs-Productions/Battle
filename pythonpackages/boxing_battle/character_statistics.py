import random
from typing import Optional
from pythonpackages.boxing_battle.fighting_move import (
    AttackMove,
    DefenseMove,
    DodgeMove,
    FightingMove,
)
from pythonpackages.boxing_battle.fighting_state import FightingState


class FightingStatistics:
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
        self.current_state = FightingState.IDLE

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
    def current_sate(self) -> FightingState:
        """The current state of the character."""
        return self._current_state

    @current_sate.setter
    def current_sate(self, value: FightingState):
        self._current_state = value

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


class OpponentStatistics(FightingStatistics):
    def __init__(
        self,
        health: int,
        stamina: int,
        recovery_percentage_stamina: float,
        idle_image: str,
        damage_imaged: str,
        defense_list: list[DefenseMove],
        attack_list: list[AttackMove],
        dodge_list: list[DodgeMove],
        state_time_defense_percentage: float = 30,
        aggression_percentage: float = 30,
        minimal_repeated_hits: int = 3,
        maximal_repeated_hits: int = 5,
        minimal_time_between_hits: float = 0.2,
        maximal_time_between_hits: float = 0.5,
        dodge_probability: float = 30,
        backlash_probability: float = 30,
        maximum_thinking_time: float = 1,
        minimal_thinking_time: float = 0.5,
    ):
        super().__init__(
            health,
            stamina,
            recovery_percentage_stamina,
            idle_image,
            damage_imaged,
        )

        self.defense_list = defense_list
        self.attack_list = attack_list
        self.dodge_list = dodge_list
        self.state_time_defense_percentage = state_time_defense_percentage
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
    def random_defense(self) -> DefenseMove:
        """Return a random defense move."""
        return random.choice(self.defense_list)

    @property
    def attack_list(self) -> list[AttackMove]:
        """The attack list of the opponent."""
        return self._attack_list

    @attack_list.setter
    def attack_list(self, value: list[AttackMove]):
        self._attack_list = value

    @property
    def random_attack(self) -> AttackMove:
        """Return a random attack move."""
        return random.choice(self.attack_list)

    @property
    def dodge_list(self) -> list[DodgeMove]:
        """The dodge list of the opponent."""
        return self._dodge_list

    @dodge_list.setter
    def dodge_list(self, value: list[DodgeMove]):
        self._dodge_list = value

    @property
    def state_time_defense_percentage(self) -> float:
        """The state time defense percentage of the opponent."""
        return self._state_time_defense_percentage

    @state_time_defense_percentage.setter
    def state_time_defense_percentage(self, value: float):
        self._state_time_defense_percentage = value

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

    def get_image(self, state: Optional[FightingMove] = None) -> str:
        """Return the image of the opponent."""
        if state is None:
            if self.current_sate == FightingState.DAMAGED:
                return self.damage_imaged
            else:
                return self.idle_image
        return state.animation_image
