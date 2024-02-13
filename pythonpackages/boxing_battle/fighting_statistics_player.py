from typing import Optional
from pythonpackages.boxing_battle.fighting_move import (
    AttackMove,
    DefenseMove,
    FightingMove,
)
from pythonpackages.boxing_battle.fighting_statistics import FightingStatistics
from pythonpackages.renpy_utility.renpy_custom_log import log_info
import renpy.exports as renpy


class PlayerStatistics(FightingStatistics):
    def __init__(
        self,
        health: int,
        stamina: int,
        recovery_percentage_stamina: float,
        idle_image: str,
        damage_imaged: str,
        x_button: Optional[FightingMove] = None,
        y_button: Optional[FightingMove] = None,
        a_button: Optional[FightingMove] = None,
        b_button: Optional[FightingMove] = None,
        up_button: Optional[FightingMove] = None,
        down_button: Optional[FightingMove] = None,
        left_button: Optional[FightingMove] = None,
        right_button: Optional[FightingMove] = None,
        time_to_wait_between_hits: float = 0.5,
    ):
        super().__init__(
            health,
            stamina,
            recovery_percentage_stamina,
            idle_image,
            damage_imaged,
        )
        self.x_button = x_button
        self.y_button = y_button
        self.a_button = a_button
        self.b_button = b_button
        self.up_button = up_button
        self.down_button = down_button
        self.left_button = left_button
        self.right_button = right_button
        self.time_to_wait_between_hits = time_to_wait_between_hits

        self.x_enabled = True
        self.y_enabled = True
        self.a_enabled = True
        self.b_enabled = True
        self.up_enabled = True
        self.down_enabled = True
        self.left_enabled = True
        self.right_enabled = True

        self.last_hit_number = 0

    def check_if_button_is_selected(self, button: FightingMove) -> bool:
        """Check if the button is selected."""
        if (
            self.current_move
            and button
            and self.current_move == button
            and self.current_move.selected
        ):
            return self.current_move.selected
        else:
            return False

    @property
    def x_button(self) -> Optional[FightingMove]:
        """The x button move."""
        if self._x_button:
            self._x_button.selected = self.check_if_button_is_selected(self._x_button)

        return self._x_button

    @x_button.setter
    def x_button(self, value: Optional[FightingMove]):
        self._x_button = value

    @property
    def y_button(self) -> Optional[FightingMove]:
        """The y button move."""
        if self._y_button:
            self._y_button.selected = self.check_if_button_is_selected(self._y_button)

        return self._y_button

    @y_button.setter
    def y_button(self, value: Optional[FightingMove]):
        self._y_button = value

    @property
    def a_button(self) -> Optional[FightingMove]:
        """The a button move."""
        if self._a_button:
            self._a_button.selected = self.check_if_button_is_selected(self._a_button)

        return self._a_button

    @a_button.setter
    def a_button(self, value: Optional[FightingMove]):
        self._a_button = value

    @property
    def b_button(self) -> Optional[FightingMove]:
        """The b button move."""
        if self._b_button:
            self._b_button.selected = self.check_if_button_is_selected(self._b_button)

        return self._b_button

    @b_button.setter
    def b_button(self, value: Optional[FightingMove]):
        self._b_button = value

    @property
    def up_button(self) -> Optional[FightingMove]:
        """The up button move."""
        if self._up_button:
            self._up_button.selected = self.check_if_button_is_selected(self._up_button)

        return self._up_button

    @up_button.setter
    def up_button(self, value: Optional[FightingMove]):
        self._up_button = value

    @property
    def down_button(self) -> Optional[FightingMove]:
        """The down button move."""
        if self._down_button:
            self._down_button.selected = self.check_if_button_is_selected(
                self._down_button
            )

        return self._down_button

    @down_button.setter
    def down_button(self, value: Optional[FightingMove]):
        self._down_button = value

    @property
    def left_button(self) -> Optional[FightingMove]:
        """The left button move."""
        if self._left_button:
            self._left_button.selected = self.check_if_button_is_selected(
                self._left_button
            )

        return self._left_button

    @left_button.setter
    def left_button(self, value: Optional[FightingMove]):
        self._left_button = value

    @property
    def right_button(self) -> Optional[FightingMove]:
        """The right button move."""
        if self._right_button:
            self._right_button.selected = self.check_if_button_is_selected(
                self._right_button
            )

        return self._right_button

    @right_button.setter
    def right_button(self, value: Optional[FightingMove]):
        self._right_button = value

    @property
    def x_enabled(self) -> bool:
        """If the x button is enabled."""
        if self.is_in_damaged_state:
            return False
        return self._x_enabled

    @x_enabled.setter
    def x_enabled(self, value: bool):
        self._x_enabled = value

    @property
    def y_enabled(self) -> bool:
        """If the y button is enabled."""
        if self.is_in_damaged_state:
            return False
        return self._y_enabled

    @y_enabled.setter
    def y_enabled(self, value: bool):
        self._y_enabled = value

    @property
    def a_enabled(self) -> bool:
        """If the a button is enabled."""
        if self.is_in_damaged_state:
            return False
        return self._a_enabled

    @a_enabled.setter
    def a_enabled(self, value: bool):
        self._a_enabled = value

    @property
    def b_enabled(self) -> bool:
        """If the b button is enabled."""
        if self.is_in_damaged_state:
            return False
        return self._b_enabled

    @b_enabled.setter
    def b_enabled(self, value: bool):
        self._b_enabled = value

    @property
    def up_enabled(self) -> bool:
        """If the up button is enabled."""
        if self.is_in_damaged_state:
            return False
        return self._up_enabled

    @up_enabled.setter
    def up_enabled(self, value: bool):
        self._up_enabled = value

    @property
    def down_enabled(self) -> bool:
        """If the down button is enabled."""
        if self.is_in_damaged_state:
            return False
        return self._down_enabled

    @down_enabled.setter
    def down_enabled(self, value: bool):
        self._down_enabled = value

    @property
    def left_enabled(self) -> bool:
        """If the left button is enabled."""
        if self.is_in_damaged_state:
            return False
        return self._left_enabled

    @left_enabled.setter
    def left_enabled(self, value: bool):
        self._left_enabled = value

    @property
    def right_enabled(self) -> bool:
        """If the right button is enabled."""
        if self.is_in_damaged_state:
            return False
        return self._right_enabled

    @right_enabled.setter
    def right_enabled(self, value: bool):
        self._right_enabled = value

    @property
    def time_to_wait_between_hits(self) -> float:
        """The time to wait between hits."""
        return self._time_to_wait_between_hits

    @time_to_wait_between_hits.setter
    def time_to_wait_between_hits(self, value: float):
        self._time_to_wait_between_hits = value

    @property
    def last_hit_number(self) -> int:
        """The last hit number."""
        return self._last_hit_number

    @last_hit_number.setter
    def last_hit_number(self, value: int):
        self._last_hit_number = value

    def disable_all_buttons(self):
        """Disable all buttons."""
        self.x_enabled = False
        self.y_enabled = False
        self.a_enabled = False
        self.b_enabled = False
        self.up_enabled = False
        self.down_enabled = False
        self.left_enabled = False
        self.right_enabled = False

    def enable_all_buttons(self):
        """Enable all buttons."""
        self.x_enabled = True
        self.y_enabled = True
        self.a_enabled = True
        self.b_enabled = True
        self.up_enabled = True
        self.down_enabled = True
        self.left_enabled = True
        self.right_enabled = True

    def set_move(self, move: Optional[FightingMove]):
        """Set the move of the player."""
        renpy.hide(self.image)
        if isinstance(self.current_move, DefenseMove):
            self.current_move.selected = False

        if isinstance(move, DefenseMove):
            log_info("DefenseMove")
            if self.current_move == move:
                self.current_move = None
            else:
                self.current_move = move
                self.current_move.selected = True
        elif isinstance(move, AttackMove):
            self.current_move = move
            self.disable_all_buttons()
            self.last_hit_number += 1
        else:
            self.current_move = move
        renpy.show(self.image)

    def after_hit(self):
        """After a hit."""
        if isinstance(self.current_move, AttackMove):
            self.current_move = None
            self.is_in_damaged_state = False
            self.enable_all_buttons()
