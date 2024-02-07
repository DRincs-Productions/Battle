init python:
    from pythonpackages.boxing_battle.fighting_state import FightingState
    from pythonpackages.boxing_battle.character_statistics import update_move

screen boxing_opponent_thinking(player, opponent):
    if not opponent.current_state == FightingState.ATTACK:
        timer opponent.random_thinking_time repeat True action [
                Function(update_move, opponent, player),
            ]
    if opponent.current_state == FightingState.ATTACK:
        timer opponent.random_time_between_hits repeat opponent.current_state == FightingState.ATTACK action [
                Function(opponent.add_hit),
                Function(player.damage, opponent.current_move),
            ]
