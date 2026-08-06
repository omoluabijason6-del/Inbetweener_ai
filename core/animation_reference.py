from dataclasses import dataclass, field


@dataclass
class AnimationReference:
    """
    Represents everything learned from
    a reference animation.
    """

    source: str

    total_frames: int

    fps: int

    animation_principles: list = field(default_factory=list)

    observations: list = field(default_factory=list)