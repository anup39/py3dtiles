from enum import Enum
from dataclasses import dataclass
from typing import Optional

class Step(Enum):
    REDUCTION = "decimation"
    SPLITTING = "splitting"
    TILING = "tiling"

@dataclass
class Options:
    input: str
    output: str
    divisions: int = 2
    lods: int = 3
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    altitude: float = 0
    scale: float = 1.0
