from dataclasses import dataclass
from uuid import UUID
from account.domain.exception import (
    InsufficientFundsException,
    SelfTransferException,
    NegativeAmountException
)
from decimal import Decimal


@dataclass
class Account:
    id: UUID
    owner_name: str
    balance: Decimal

    def transfer_to(self, target_account: 'Account', amount: Decimal) -> None:
        self._validate_transfer(target_account, amount)
        self.balance -= amount
        target_account.balance += amount

    def _validate_transfer(self, target_account: 'Account', amount: Decimal) -> None:
        if amount <= 0:
            raise NegativeAmountException("Transfer amount must be positive")
        if self.id == target_account.id:
            raise SelfTransferException("Cannot transfer to the same account")
        if self.balance < amount:
            raise InsufficientFundsException(
                f"Insufficient funds. Available: {self.balance}, required: {amount}"
            )
