init python:
    from pythonpackages.boxing_battle.fighting_state import FightingState
    from pythonpackages.boxing_battle.fighting_fun import update_opponent_move, update_opponent_hit

screen boxing_opponent_thinking(player, opponent):
    if not opponent.current_state == FightingState.ATTACK:
        timer opponent.random_thinking_time repeat True action [
                Function(update_opponent_move, opponent, player),
            ]
    else:
        timer opponent.random_time_between_hits repeat opponent.current_state == FightingState.ATTACK action [
                Function(update_opponent_hit, opponent, player),
            ]
