from dataclasses import dataclass


@dataclass
class Keyframe:
    """
    Represents a single keyframe in an animation.
    """

    frame_number: int

    image_path: str

    description: str = ""