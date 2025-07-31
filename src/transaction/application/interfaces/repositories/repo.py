from abc import ABC, abstractmethod
from transaction.domain.entity import Transaction


class ITransactionRepository(ABC):

    @abstractmethod
    def save(self, entity: Transaction) -> Transaction:
        pass
