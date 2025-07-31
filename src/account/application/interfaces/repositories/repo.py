from abc import ABC, abstractmethod
from uuid import UUID
from typing import List
from account.domain.entity import Account


class IAccountRepository(ABC):

    @abstractmethod
    def save(self, entity: Account) -> Account:
        pass

    @abstractmethod
    def get_by_id(self, id: UUID) -> Account:
        pass

    @abstractmethod
    def list_all(self) -> List[Account]:
        pass
