from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Person:
    name: str
    age: int
    email: Optional[str] = None
    skills: List[str] = None

    def __post_init__(self):
        if self.skills is None:
            self.skills = []
        if self.age < 0:
            raise ValueError("Age cannot be negative")

# Usage:
john = Person("John Doe", 30, "john@example.com", ["Python", "Django"])
jane = Person("Jane Smith", 25, skills=["JavaScript", "React"])

# Automatic equality comparison:
john == Person("John Doe", 30, "john@example.com", ["Python", "Django"]) # True