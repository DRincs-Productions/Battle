init -10 python:
    from pythonpackages.boxing_battle.fighting_state import FightingState

default opponent_state = FightingState.IDLE

screen boxing_battle(player_statistics, opponent_statistics):
    # ...
    use boxing_battle_opponent(opponent_statistics)

screen boxing_battle_opponent(opponent_statistics):
    # Defence
    timer opponent_statistics.random_thinking_time:
        action [
            # opponent_statistics.random_defense ... 
        ]
    # Attack
    timer opponent_statistics.random_thinking_time:
        action [
            # opponent_statistics.random_attack ... 
        ]
