import random
from typing import Optional, Union
from pythonpackages.boxing_battle.fighting_move import (
    AttackMove,
    DefenseMove,
    DodgeMove,
    FightingMove,
)
from pythonpackages.boxing_battle.fighting_state import FightingState
from pythonpackages.boxing_battle.fighting_statistics import FightingStatistics
from pythonpackages.renpy_utility.renpy_custom_log import log_info, log_warn
import renpy.exports as renpy


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
            if move is not None and self.stamina >= move.stamina_cost:
                log_info("ATTACK")
                self.current_hit_number = 1
                log_info("HIT: " + str(self.current_hit_number))
                self.stamina -= move.stamina_cost
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

    def add_hit(self) -> bool:
        """Add a hit to the opponent."""
        if not isinstance(self.current_move, AttackMove):
            log_warn(
                "The current move is not an attack move.", "OpponentStatistics.add_hit"
            )
            return False
        res = False
        renpy.hide(self.image)
        if (
            self.stamina >= self.current_move.stamina_cost
            and self.current_hit_number <= self.random_repeated_hits
        ):
            self.stamina -= self.current_move.stamina_cost
            self.current_hit_number += 1
            res = True
            log_info("HIT: " + str(self.current_hit_number))
        else:
            self.current_hit_number = 0
            self.current_move = self.random_defense
            res = False
            log_info("DEFENSE")
        renpy.show(self.image)
        return res
