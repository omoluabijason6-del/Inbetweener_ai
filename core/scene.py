from dataclasses import dataclass, field


@dataclass
class Scene:
    """
    Represents one animation scene.
    """

    name: str

    frame_rate: int = 24

    duration: int = 0

    characters: list = field(default_factory=list)

    keyframes: list = field(default_factory=list)