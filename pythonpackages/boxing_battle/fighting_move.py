from typing import Optional


class FightingMove:
    def __init__(
        self,
        name: str,
        icon: str,
        anination_image: str,
        animation_time: Optional[float] = None,
        animation_sound: Optional[str] = None,
    ):
        self.name = name
        self.icon = icon
        self.animation_image = anination_image
        self.animation_time = animation_time
        self.animation_sound = animation_sound

    @property
    def name(self) -> str:
        """The name of the move."""
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def icon(self) -> str:
        """The icon of the move."""
        return self._icon

    @icon.setter
    def icon(self, value: str):
        self._icon = value

    @property
    def animation_image(self) -> str:
        """The image of the move."""
        return self._animation_image

    @animation_image.setter
    def animation_image(self, value: str):
        self._animation_image = value

    @property
    def animation_time(self) -> float:
        """The time of the move."""
        if self._animation_time is None:
            return 0.0
        return self._animation_time

    @animation_time.setter
    def animation_time(self, value: Optional[float]):
        self._animation_time = value

    @property
    def animation_sound(self) -> Optional[str]:
        """The sound of the move."""
        return self._animation_sound

    @animation_sound.setter
    def animation_sound(self, value: Optional[str]):
        self._animation_sound = value


class AttackMove(FightingMove):
    def __init__(
        self,
        name: str,
        icon: str,
        health_damage: int,
        stamina_damage: int,
        anination_image: str,
        animation_time: Optional[float] = None,
        animation_sound: Optional[str] = None,
        stum_time: Optional[float] = None,
    ):
        super().__init__(
            name=name,
            icon=icon,
            anination_image=anination_image,
            animation_time=animation_time,
            animation_sound=animation_sound,
        )

        self.health_damage = health_damage
        self.stamina_damage = stamina_damage
        self.stum_time = stum_time

    @property
    def health_damage(self) -> int:
        """The health damage of the move."""
        return self._health_damage

    @health_damage.setter
    def health_damage(self, value: int):
        self._health_damage = value

    @property
    def stamina_damage(self) -> int:
        """The stamina damage of the move."""
        return self._stamina_damage

    @stamina_damage.setter
    def stamina_damage(self, value: int):
        self._stamina_damage = value

    @property
    def stum_time(self) -> float:
        """The stun time of the move."""
        if self._stum_time is None:
            return 0.0
        return self._stum_time

    @stum_time.setter
    def stum_time(self, value: Optional[float]):
        self._stum_time = value


class DefenseMove(FightingMove):
    def __init__(
        self,
        name: str,
        icon: str,
        anination_image: str,
        animation_time: Optional[float] = None,
        animation_sound: Optional[str] = None,
        life_resistance_percentage: Optional[float] = None,
        stamina_resistance_percentage: Optional[float] = None,
    ):
        super().__init__(
            name=name,
            icon=icon,
            anination_image=anination_image,
            animation_time=animation_time,
            animation_sound=animation_sound,
        )

        self.life_resistance_percentage = life_resistance_percentage
        self.stamina_resistance_percentage = stamina_resistance_percentage

    @property
    def life_resistance_percentage(self) -> float:
        """
        The life resistance percentage of the move.
        Default is 100%.
        """
        if self._life_resistance_percentage is None:
            return 100.0
        return self._life_resistance_percentage

    @life_resistance_percentage.setter
    def life_resistance_percentage(self, value: Optional[float]):
        self._life_resistance_percentage = value

    @property
    def stamina_resistance_percentage(self) -> float:
        """
        The stamina resistance percentage of the move.
        Default is 0%.
        """
        if self._stamina_resistance_percentage is None:
            return 0.0
        return self._stamina_resistance_percentage

    @stamina_resistance_percentage.setter
    def stamina_resistance_percentage(self, value: Optional[float]):
        self._stamina_resistance_percentage = value
