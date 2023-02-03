"""
create dataclass `Engine`
"""
from dataclasses import dataclass, asdict, astuple, field


@dataclass
class Engine:
    volume: int
    pistons: int
