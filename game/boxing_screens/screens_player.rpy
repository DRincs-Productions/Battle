screen boxing_player_thinking(player, opponent):
    if player.is_in_damaged_state:
        timer player.stun_time_to_wait_into_timer repeat player.is_in_damaged_state action [
                Function(player.remove_damage_state),
            ]
    timer player.time_to_wait_between_hits repeat True action [
            Function(player.after_hit),
        ]
