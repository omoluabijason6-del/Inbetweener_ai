from dataclasses import dataclass, field


@dataclass
class GenerationRequest:
    """
    Everything needed to generate
    one in-between frame.
    """

    start_image: str

    end_image: str

    target_frame: int

    prompt: str

    negative_prompt: str

    notes: list = field(default_factory=list)