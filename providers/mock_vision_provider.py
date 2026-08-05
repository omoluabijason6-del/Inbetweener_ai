from core.analysis_result import AnalysisResult
from core.vision_provider import VisionProvider


class MockVisionProvider(VisionProvider):
    """
    Fake AI provider.

    Used until we connect a real model.
    """

    def analyze(self, image_path: str) -> AnalysisResult:

        print("[Mock AI] Looking at image...")

        return AnalysisResult(
            character_name="Bipo",
            pose="Standing",
            facial_expression="Happy",
            camera_angle="Front",
            movement_direction="None",
            confidence=0.98,
            observations=[
                "Character centered",
                "Clean outline",
                "Simple pose"
            ]
        )