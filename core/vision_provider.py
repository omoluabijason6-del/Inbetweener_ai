from abc import ABC, abstractmethod

from core.analysis_result import AnalysisResult


class VisionProvider(ABC):
    """
    Base interface for every
    AI Vision Provider.
    """

    @abstractmethod
    def analyze(
        self,
        image_path: str
    ) -> AnalysisResult:
        """
        Analyze one animation keyframe.
        """
        pass