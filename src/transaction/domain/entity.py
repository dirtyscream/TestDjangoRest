# transaction/domain/entity.py
from dataclasses import dataclass, field
from uuid import UUID
from decimal import Decimal
from datetime import datetime


@dataclass
class Transaction:
    id: UUID
    from_account: 'Account'
    to_account: 'Account'
    amount: Decimal
    created_at: datetime
    timestamp: datetime = field(default_factory=datetime.now)
