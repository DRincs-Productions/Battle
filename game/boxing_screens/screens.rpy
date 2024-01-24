﻿default opponent_image = None
default opponent_move = None

screen boxing_battle(player_statistics, opponent_statistics):
    # ...
    use boxing_battle_opponent(opponent_statistics)

screen boxing_battle_opponent(opponent_statistics):
    $ opponent_image = opponent_statistics.get_image()
    $ opponent_move = None

    add opponent_image
    timer opponent_statistics.random_thinking_time:
        action [
            SetVariable(opponent_move, opponent_statistics.get_move(opponent_move)),
            SetVariable(opponent_image, opponent_statistics.get_image(opponent_move)) 
        ]
