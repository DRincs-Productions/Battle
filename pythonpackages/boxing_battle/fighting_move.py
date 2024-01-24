from typing import Optional


class FightingMove:
    def __init__(
        self,
        name: str,
        icon: str,
        key: str,
        animation_image: str,
        animation_time: Optional[float] = None,
        animation_sound: Optional[str] = None,
        can_be_pressed: bool = True,
    ):
        self.name = name
        self.icon = icon
        self.key = key
        self.animation_image = animation_image
        self.animation_time = animation_time
        self.animation_sound = animation_sound
        self.can_be_pressed = can_be_pressed

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
    def key(self) -> str:
        """The key of the move."""
        return self._key

    @key.setter
    def key(self, value: str):
        self._key = value

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

    @property
    def can_be_pressed(self) -> bool:
        """If the move can be pressed."""
        return self._can_be_pressed

    @can_be_pressed.setter
    def can_be_pressed(self, value: bool):
        self._can_be_pressed = value


class AttackMove(FightingMove):
    def __init__(
        self,
        name: str,
        icon: str,
        key: str,
        health_damage: int,
        stamina_damage: int,
        animation_image: str,
        required_stamina: int,
        animation_time: Optional[float] = None,
        animation_sound: Optional[str] = None,
        stum_time: Optional[float] = None,
    ):
        super().__init__(
            name=name,
            icon=icon,
            key=key,
            animation_image=animation_image,
            animation_time=animation_time,
            animation_sound=animation_sound,
            can_be_pressed=False,
        )

        self.health_damage = health_damage
        self.stamina_damage = stamina_damage
        self.stum_time = stum_time
        self.required_stamina = required_stamina

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

    @property
    def required_stamina(self) -> int:
        """The required stamina of the move."""
        return self._required_stamina

    @required_stamina.setter
    def required_stamina(self, value: int):
        self._required_stamina = value


class DefenseMove(FightingMove):
    def __init__(
        self,
        name: str,
        icon: str,
        key: str,
        animation_image: str,
        animation_time: Optional[float] = None,
        animation_sound: Optional[str] = None,
        health_resistance: Optional[int] = None,
        stamina_resistance: Optional[int] = None,
    ):
        super().__init__(
            name=name,
            icon=icon,
            key=key,
            animation_image=animation_image,
            animation_time=animation_time,
            animation_sound=animation_sound,
            can_be_pressed=True,
        )

        self.health_resistance = health_resistance
        self.stamina_resistance = stamina_resistance

    @property
    def health_resistance(self) -> int:
        """
        The health resistance of the move.
        Default is 999999.
        """
        if self._health_resistance is None:
            return 999999
        return self._health_resistance

    @health_resistance.setter
    def health_resistance(self, value: Optional[int]):
        self._health_resistance = value

    @property
    def stamina_resistance(self) -> int:
        """
        The stamina resistance of the move.
        Default is 0.
        """
        if self._stamina_resistance is None:
            return 0
        return self._stamina_resistance

    @stamina_resistance.setter
    def stamina_resistance(self, value: Optional[int]):
        self._stamina_resistance = value


class DodgeMove(FightingMove):
    def __init__(
        self,
        name: str,
        icon: str,
        key: str,
        effect_time: float,
        animation_image: str,
        animation_sound: Optional[str] = None,
    ):
        super().__init__(
            name=name,
            icon=icon,
            key=key,
            animation_image=animation_image,
            animation_time=effect_time,
            animation_sound=animation_sound,
            can_be_pressed=False,
        )
