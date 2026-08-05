from core.vision_provider import VisionProvider


class VisionAgent:
    """
    AI Vision Agent.
    """

    def __init__(self, provider: VisionProvider):
        self.name = "Vision Agent"
        self.provider = provider

    def start(self):
        print("[Vision] Ready.")

    def analyze_keyframe(self, image_path):
        print(f"[Vision] Sending {image_path} to AI...")

        return self.provider.analyze(image_path)