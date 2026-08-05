from dataclasses import dataclass, field


@dataclass
class AnalysisResult:
    """
    Stores everything the Vision Agent learns
    from one keyframe.
    """

    character_name: str

    pose: str

    facial_expression: str

    camera_angle: str

    movement_direction: str

    confidence: float

    observations: list = field(default_factory=list)