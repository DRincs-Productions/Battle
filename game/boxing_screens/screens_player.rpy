screen boxing_player_thinking(player, opponent):
    if player.stun_time_to_wait > 0:
        timer player.stun_time_to_wait repeat player.stun_time_to_wait > 0 action [
                Function(renpy.hide, player.image),
                Function(player.remove_damage_state),
                Function(renpy.show, player.image),
            ]
