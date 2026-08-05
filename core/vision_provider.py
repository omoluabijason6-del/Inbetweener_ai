from abc import ABC, abstractmethod

from core.analysis_result import AnalysisResult


class VisionProvider(ABC):
    """
    Base class for every AI vision provider.
    """

    @abstractmethod
    def analyze(self, image_path: str) -> AnalysisResult:
        pass