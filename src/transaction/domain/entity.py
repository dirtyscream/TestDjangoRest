from dataclasses import dataclass
from uuid import UUID
from decimal import Decimal
from datetime import datetime
from account.domain.entity import Account


@dataclass
class Transaction:
    id: UUID
    from_account: Account
    to_account: Account
    amount: Decimal
    created_at: datetime
