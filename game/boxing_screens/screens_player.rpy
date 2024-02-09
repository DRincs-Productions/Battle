screen boxing_player_thinking(player, opponent):
    if player.stun_time_to_wait > 0:
        timer player.stun_time_to_wait repeat player.stun_time_to_wait > 0 action [
                Function(player.remove_damage_state),
            ]
    elif opponent.current_state == FightingState.ATTACK:
        timer player.time_to_wait_between_hits repeat False action [
                Function(player.after_hit),
            ]
