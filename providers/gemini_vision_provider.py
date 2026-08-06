import json
import os
from pathlib import Path

from google import genai
from google.genai import types

from core.analysis_result import AnalysisResult
from core.vision_provider import VisionProvider
from core.animator_prompt import ANIMATOR_PROMPT


class GeminiVisionProvider(VisionProvider):
    """
    Uses Google Gemini to analyze
    animation keyframes.
    """

    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY environment variable not found."
            )

        self.client = genai.Client(api_key=api_key)
        self.model = "gemini-3.6-flash"

    def analyze(self, image_path: str) -> AnalysisResult:

        print("[Gemini] Sending image for analysis...")

        image_bytes = Path(image_path).read_bytes()

        prompt = ANIMATOR_PROMPT

        response = self.client.models.generate_content(
            model=self.model,
            contents=[
                prompt,
                types.Part.from_bytes(
                    data=image_bytes,
                    mime_type="image/png"
                )
            ]
        )

        text = response.text.strip()

        if text.startswith("```"):
            text = text.replace("```json", "")
            text = text.replace("```", "")
            text = text.strip()
        print("\n===== GEMINI RAW RESPONSE =====")
        print(text)
        print("===== END RESPONSE =====\n")
        try:
            data = json.loads(text)
        except json.JSONDecodeError:
            print("Gemini did not return valid JSON.")
            print(text)
            return AnalysisResult(
            pose="Unknown",
            expression="Unknown"
    )

        return AnalysisResult(**data)