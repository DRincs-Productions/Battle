init python:
    from pythonpackages.boxing_battle.fighting_state import FightingState
    from pythonpackages.extra_animated_value.extra_animated_value import ExtraAnimatedValue
    from pythonpackages.extra_animated_value.value_image import ValueImage

screen boxing_battle(opponent, recover_time = 10):
    $ bar_opponent_health = ExtraAnimatedValue(
            value=opponent.health, 
            range=opponent.max_health, 
            range_delay=3.0,
            warper="ease_quart",
        )
    $ bar_opponent_stamina = ExtraAnimatedValue(
            value=opponent.stamina, 
            range=opponent.max_stamina, 
            range_delay=3.0,
            warper="ease_quart",
        )

    vbox:
        spacing 10
        align (0.98, 0.02)

        use health_bar(bar_opponent_health)
        use stamina_bar(bar_opponent_stamina)

    # ...
    use boxing_battle_opponent(opponent)
    timer recover_time repeat True action [
            Function(opponent.recover_stamina),
        ]

screen boxing_battle_opponent(opponent):
    $ renpy.show(opponent.image)
    timer opponent.random_thinking_time repeat True action [
            Function(renpy.hide, opponent.image),
            Function(opponent.update_move),
            Function(renpy.show, opponent.image),
        ]
    if opponent.current_state == FightingState.ATTACK:
        timer opponent.random_time_between_hits repeat opponent.current_state == FightingState.ATTACK action [
                Function(renpy.hide, opponent.image),
                Function(opponent.add_hit),
                Function(renpy.show, opponent.image),
            ]

screen health_bar(my_bar):
    fixed:
        area (0,0, 400, 50)
        bar:
            value my_bar
            left_bar "images/bar/health_bar_400x50_left.png"
            right_bar "images/bar/health_bar_400x50_right.png"
            area (0,0, 400, 50)

        add my_bar.text(
            "{0.current_value:.0f} hp",
            size = 22,
            color = "#FFF",
            outlines = [(abs(2), "#000")],
            bold = True,
            xcenter = 0.5,
            ycenter = 0.57)

screen stamina_bar(my_bar):
    fixed:
        area (0,0, 400, 50)
        bar:
            value my_bar
            left_bar "images/bar/health_bar_400x50_left.png"
            right_bar "images/bar/health_bar_400x50_right.png"
            area (0,0, 400, 50)

        add my_bar.text(
            "{0.current_value:.0f}/{0.range:.0f}",
            size = 22,
            color = "#DDE",
            outlines = [(abs(1), "#222")],
            bold = True,
            xcenter = 0.5,
            ycenter = 0.5)
