from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Project:
    """
    Represents one animation project.
    """

    name: str

    fps: int = 24

    created_at: str = field(
        default_factory=lambda: datetime.now().isoformat()
    )

    scenes: list = field(default_factory=list)