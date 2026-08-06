from core.analysis_result import AnalysisResult
from core.vision_provider import VisionProvider


class MockVisionProvider(VisionProvider):
    """
    Temporary AI provider.

    This simulates what a future
    multimodal AI model will return.
    """

    def analyze(self, image_path):

        print("[Mock AI] Looking at image...")

        return AnalysisResult(
            character_name="Bipo",

            pose="Standing",

            facial_expression="Happy",

            camera_angle="Front",

            movement_direction="None",

            confidence=0.98,

            line_of_action="Vertical",

            balance="Centered",

            silhouette="Very Clear",

            squash_stretch="None",

            anticipation="Minimal",

            follow_through="None",

            appeal="High",

            staging="Character centered",

            observations=[
                "Head is circular",
                "Eyes are symmetrical",
                "Pose is readable",
                "Center of gravity is stable",
                "Clean outline",
                "Good spacing"
            ]
        )