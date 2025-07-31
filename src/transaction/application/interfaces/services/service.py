from transaction.domain.entity import Transaction
from abc import ABC, abstractmethod
from uuid import UUID
from decimal import Decimal


class ITransactionService(ABC):

    @abstractmethod
    def execute_transfer(self,
                         from_account: UUID,
                         to_account: UUID,
                         amount: Decimal) -> Transaction:
        pass
