init python:
    from pythonpackages.boxing_battle.fighting_state import FightingState

screen boxing_battle(player_statistics, opponent):
    # ...
    use boxing_battle_opponent(opponent)

screen boxing_battle_opponent(opponent):
    $ renpy.show(opponent.image)
    timer opponent.random_thinking_time repeat True action [
            Function(renpy.hide, opponent.image),
            Function(opponent.update_move),
            Function(renpy.show, opponent.image),
        ]
    # if opponent.current_state == FightingState.ATTACK:
    #     timer opponent.random_time_between_hits repeat opponent.current_state == FightingState.ATTACK action [
    #             Function(opponent.add_hit),
    #         ]
