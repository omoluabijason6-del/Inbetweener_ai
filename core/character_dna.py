from dataclasses import dataclass, field


@dataclass
class CharacterDNA:
    """
    Stores the rules that define a character.
    """

    name: str

    head_shape: str

    eye_shape: str

    body_height: float

    outline_style: str

    colors: list = field(default_factory=list)