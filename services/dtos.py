from dataclasses import dataclass

@dataclass
class ServiceDTO:
    id: int
    name: str
    description: str
    category: str
    is_active: bool
