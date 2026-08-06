from dataclasses import dataclass, field


@dataclass
class AnalysisResult:
    """
    Stores everything the Vision Agent learns
    from one animation keyframe.
    """

    pose: str = ""
    expression: str = ""

    head_rotation: str = ""
    torso_rotation: str = ""

    left_arm: str = ""
    right_arm: str = ""

    left_leg: str = ""
    right_leg: str = ""

    weight_distribution: str = ""
    center_of_gravity: str = ""

    balance: str = ""
    line_of_action: str = ""

    silhouette: str = ""

    anticipation: str = ""
    squash_stretch: str = ""
    follow_through: str = ""

    appeal: str = ""
    staging: str = ""

    camera_angle: str = ""
    movement_direction: str = ""

    strengths: list = field(default_factory=list)
    weaknesses: list = field(default_factory=list)
    suggestions: list = field(default_factory=list)

    animation_score: int = 0