init python:
    from pythonpackages.boxing_battle.fighting_state import FightingState

screen boxing_opponent_thinking(player, opponent):
    if not opponent.current_state == FightingState.ATTACK:
        timer opponent.random_thinking_time repeat True action [
                Function(renpy.hide, player.image),
                Function(renpy.hide, opponent.image),
                Function(opponent.update_move, player),
                Function(renpy.show, player.image),
                Function(renpy.show, opponent.image),
            ]
    if opponent.current_state == FightingState.ATTACK:
        timer opponent.random_time_between_hits repeat opponent.current_state == FightingState.ATTACK action [
                Function(renpy.hide, player.image),
                Function(renpy.hide, opponent.image),
                Function(opponent.add_hit),
                Function(player.damage, opponent.current_move),
                Function(renpy.show, player.image),
                Function(renpy.show, opponent.image),
            ]
