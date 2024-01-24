default opponent_state = "defense"

screen boxing_battle(player_statistics, opponent_statistics):
    # ...
    use boxing_battle_opponent(opponent_statistics)

screen boxing_battle_opponent(opponent_statistics):
    # Defence
    timer opponent_statistics.random_thinking_time:
        action opponent_statistics.random_thinking_time [
            # opponent_statistics.random_defense ... 
        ]
    # Attack
    timer opponent_statistics.random_thinking_time:
        action opponent_statistics.random_thinking_time [
            # opponent_statistics.random_attack ... 
        ]