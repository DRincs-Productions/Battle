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
