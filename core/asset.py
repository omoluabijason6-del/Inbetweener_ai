from dataclasses import dataclass


@dataclass
class Asset:
    """
    Represents a file used by the project.
    """

    name: str

    path: str

    asset_type: str