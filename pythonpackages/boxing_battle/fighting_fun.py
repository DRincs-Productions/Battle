from typing import Optional
from pythonpackages.boxing_battle.fighting_move import AttackMove, FightingMove
from pythonpackages.boxing_battle.fighting_statistics_opponent import OpponentStatistics
from pythonpackages.boxing_battle.fighting_statistics_player import PlayerStatistics


def update_opponent_move(opponent: OpponentStatistics, player: PlayerStatistics):
    value = opponent.update_move()
    if value and isinstance(value, AttackMove):
        player.damage(value)


def update_opponent_hit(opponent: OpponentStatistics, player: PlayerStatistics):
    res = opponent.add_hit()
    if res:
        player.damage(opponent.current_move)


def update_player_move(
    move: Optional[FightingMove], player: PlayerStatistics, opponent: OpponentStatistics
):
    player.set_move(move)
