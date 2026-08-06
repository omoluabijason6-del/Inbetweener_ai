from core.motion_plan import MotionPlan


class MotionAgent:
    """
    Creates a motion blueprint
    between two keyframes.
    """

    def __init__(self):
        self.name = "Motion Agent"

    def start(self):
        print("[Motion] Ready.")

    def create_motion_plan(
        self,
        start_keyframe,
        end_keyframe,
        reference_analysis
    ):
        print(
            f"[Motion] Planning movement "
            f"{start_keyframe.frame_number}"
            f" -> "
            f"{end_keyframe.frame_number}"
        )

        total_inbetweens = (
            end_keyframe.frame_number
            - start_keyframe.frame_number
            - 1
        )

        return MotionPlan(
            start_frame=start_keyframe.frame_number,
            end_frame=end_keyframe.frame_number,
            total_inbetweens=total_inbetweens,
            motion_type="Jump",

            spacing="Ease Out -> Ease In",

            timing="Fast Takeoff, Slow Landing",

            arc="Upward Arc",

            notes=[
                "Use anticipation",
                "Maintain silhouette",
                "Keep head volume constant",
                "Follow reference timing"
            ]
        )