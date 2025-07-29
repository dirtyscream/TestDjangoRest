import uuid
from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass(kw_only=True)
class Account:
    id: Optional[uuid.UUID] = None
    owner_name: str
    balance: float
    created_at: datetime

    def __eq__(self, other):
        if isinstance(other, Account):
            return self.id == other.id
        return False

    def __hash__(self):
        return hash(self.id) if self.id else 0
