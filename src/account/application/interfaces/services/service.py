from abc import ABC, abstractmethod
from uuid import UUID
from typing import List
from decimal import Decimal
from account.domain.entity import Account


class IAccountService(ABC):

    @abstractmethod
    def get_account(self, account_id: UUID) -> Account:
        pass

    @abstractmethod
    def get_all_accounts(self) -> List[Account]:
        pass

    @abstractmethod
    def create_account(self, owner_name: str, balance: Decimal) -> Account:
        pass
