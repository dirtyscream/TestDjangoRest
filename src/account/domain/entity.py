from dataclasses import dataclass, field
from uuid import UUID
from account.domain.exception import (
    InsufficientFundsException,
    SelfTransferException,
    NegativeAmountException,
    DailyTransferLimitExceeded
)
from decimal import Decimal
from datetime import datetime, timedelta
from transaction.domain.entity import Transaction


@dataclass
class Account:
    id: UUID
    owner_name: str
    balance: Decimal
    created_at: datetime
    transactions: list[Transaction] = field(
        default_factory=list)

    def transfer_to(self, target_account: 'Account', amount: Decimal) -> None:
        self._validate_transfer(target_account, amount)
        self.balance -= amount
        target_account.balance += amount

    def __post_init__(self):
        self._validate_balance()

    def _validate_balance(self):
        if self.balance < 0:
            raise NegativeAmountException("Account balance must be positive")

    def _validate_transfer(self, target_account: 'Account', amount: Decimal) -> None:
        if amount <= 0:
            raise NegativeAmountException("Transfer amount must be positive")
        if self.id == target_account.id:
            raise SelfTransferException("Cannot transfer to the same account")
        if self.balance < amount:
            raise InsufficientFundsException(
                f"Insufficient funds. Available: {self.balance}, required: {amount}"
            )
