from dataclasses import dataclass, field

from core.keyframe import Keyframe


@dataclass
class Scene:
    """
    Represents one animation scene.
    """

    name: str

    frame_rate: int = 24

    duration: int = 0

    characters: list = field(default_factory=list)

    keyframes: list[Keyframe] = field(default_factory=list)
    """
    Represents one animation scene.
    """

    name: str

    frame_rate: int = 24

    duration: int = 0

    characters: list = field(default_factory=list)

    keyframes: list = field(default_factory=list)