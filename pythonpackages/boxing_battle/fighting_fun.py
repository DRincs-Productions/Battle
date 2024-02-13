from typing import Optional
from pythonpackages.boxing_battle.character_statistics import (
    OpponentStatistics,
    PlayerStatistics,
)
from pythonpackages.boxing_battle.fighting_move import AttackMove, FightingMove


def update_opponent_move(opponent: OpponentStatistics, player: PlayerStatistics):
    value = opponent.update_move()
    if value and isinstance(value, AttackMove):
        player.damage(value)


def update_player_move(
    move: Optional[FightingMove], player: PlayerStatistics, opponent: OpponentStatistics
):
    player.set_move(move)
