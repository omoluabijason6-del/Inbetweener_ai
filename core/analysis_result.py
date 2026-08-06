from dataclasses import dataclass, field


@dataclass
class AnalysisResult:
    """
    Stores everything the AI learns
    from one keyframe.
    """

    character_name: str

    pose: str

    facial_expression: str

    camera_angle: str

    movement_direction: str

    confidence: float

    # Animator's Eye

    line_of_action: str

    balance: str

    silhouette: str

    squash_stretch: str

    anticipation: str

    follow_through: str

    appeal: str

    staging: str

    observations: list = field(default_factory=list)
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