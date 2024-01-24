from enum import Enum


class FightingState(Enum):
    ATTACK = 0
    DEFENSE = 1
    IDLE = 2
    DAMAGED = 3
