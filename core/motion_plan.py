from dataclasses import dataclass, field


@dataclass
class MotionPlan:
    """
    Describes how a character should move
    between two keyframes.
    """

    start_frame: int

    end_frame: int

    total_inbetweens: int

    motion_type: str

    spacing: str

    timing: str

    arc: str

    notes: list = field(default_factory=list)