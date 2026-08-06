from core.animation_reference import AnimationReference


class ReferenceAgent:
    """
    Learns animation principles from
    reference animations.
    """

    def __init__(self):
        self.name = "Reference Agent"

    def start(self):
        print("[Reference] Ready.")

    def analyze_reference(
        self,
        source,
        total_frames,
        fps
    ):
        print(f"[Reference] Analyzing {source}")

        return AnimationReference(
            source=source,
            total_frames=total_frames,
            fps=fps,
            animation_principles=[
                "Timing",
                "Spacing",
                "Arcs",
                "Squash and Stretch",
                "Anticipation",
                "Follow Through",
                "Slow In",
                "Slow Out"
            ],
            observations=[
                "Fast anticipation before jump",
                "Smooth landing arc",
                "Consistent spacing",
                "Strong silhouette"
            ]
        )