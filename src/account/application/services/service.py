from uuid import UUID
from typing import List
from decimal import Decimal
from account.domain.entity import Account
from account.domain.exception import AccountNotFoundException
from account.infrastructure.database.models import AccountModel
from account.infrastructure.database.repository.rdb import AccountRepository
from account.application.interfaces.services.service import IAccountService
from django.utils import timezone


class AccountService(IAccountService):
    repository = AccountRepository()

    def get_account(self, account_id: UUID) -> Account:
        try:
            return self.repository.get_by_id(account_id)
        except AccountModel.DoesNotExist:
            raise AccountNotFoundException(f"Account {account_id} not found")

    def get_all_accounts(self) -> List[Account]:
        return self.repository.list_all()

    def create_account(self, owner_name: str, balance: Decimal) -> Account:
        account = Account(
            id=None,
            owner_name=owner_name,
            balance=balance,
            created_at=timezone.now()
        )
        return self.repository.save(account)
