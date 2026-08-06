import json
from pathlib import Path

from google import genai

from core.analysis_result import AnalysisResult
from core.vision_provider import VisionProvider


class GeminiVisionProvider(VisionProvider):
    """
    Google Gemini Vision Provider.
    """

    def __init__(self):
        self.client = genai.Client()
        self.model = "gemini-2.5-flash"

    def analyze(self, image_path: str) -> AnalysisResult:

        print("[Gemini] Analyzing image...")

        image_bytes = Path(image_path).read_bytes()

        prompt = """
You are an expert 2D animation supervisor.

Analyze this hand-drawn animation keyframe.

Return ONLY valid JSON with these fields:

{
  "character_name": "",
  "pose": "",
  "facial_expression": "",
  "camera_angle": "",
  "movement_direction": "",
  "confidence": 0.0,
  "line_of_action": "",
  "balance": "",
  "silhouette": "",
  "squash_stretch": "",
  "anticipation": "",
  "follow_through": "",
  "appeal": "",
  "staging": "",
  "observations": []
}
"""

        response = self.client.models.generate_content(
            model=self.model,
            contents=[
                {
                    "text": prompt
                },
                {
                    "inline_data": {
                        "mime_type": "image/png",
                        "data": image_bytes
                    }
                }
            ]
        )

        data = json.loads(response.text)

        return AnalysisResult(**data)