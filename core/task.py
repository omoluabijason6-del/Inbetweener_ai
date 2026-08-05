from dataclasses import dataclass
from typing import Any


@dataclass
class Task:
    """
    Represents a single unit of work.
    """

    id: int

    name: str

    priority: int = 5

    data: Any = None