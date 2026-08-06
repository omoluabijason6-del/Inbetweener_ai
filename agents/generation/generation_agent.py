from core.generation_request import GenerationRequest


class GenerationAgent:
    """
    Creates generation requests
    for future AI image models.
    """

    def __init__(self):
        self.name = "Generation Agent"

    def start(self):
        print("[Generation] Ready.")

    def create_request(
        self,
        start_keyframe,
        end_keyframe,
        vision_result,
        reference,
        motion_plan
    ):

        print("[Generation] Building request...")

        prompt = (
            f"Generate frame between "
            f"{start_keyframe.frame_number} "
            f"and "
            f"{end_keyframe.frame_number}. "
            f"Character: {vision_result.character_name}. "
            f"Pose: {vision_result.pose}. "
            f"Motion: {motion_plan.motion_type}. "
            f"Timing: {motion_plan.timing}. "
            f"Spacing: {motion_plan.spacing}. "
            f"Arc: {motion_plan.arc}. "
            f"Preserve the original hand-drawn style."
        )

        negative_prompt = (
            "Do not change the character design. "
            "Do not add extra limbs. "
            "Do not change colors. "
            "Do not change camera angle. "
            "Do not add background objects."
        )

        return GenerationRequest(
            start_image=start_keyframe.image_path,
            end_image=end_keyframe.image_path,
            target_frame=2,
            prompt=prompt,
            negative_prompt=negative_prompt,
            notes=[
                "Maintain character consistency",
                "Keep line thickness consistent",
                "Follow reference animation principles",
                "Maintain silhouette",
                "Preserve hand-drawn appearance"
            ]
        )