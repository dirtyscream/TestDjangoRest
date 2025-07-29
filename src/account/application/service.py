from typing import Optional
import uuid
from account.infrastructure.database.models import AccountModel
from account.domain.entity import Account
from account.domain.exception import AccountNotFoundException


class AccountService:
    def get_account(self, account_id: uuid.UUID) -> AccountModel:
        try:
            return AccountModel.objects.get(id=account_id)
        except AccountModel.DoesNotExist:
            raise AccountNotFoundException(f"Account {account_id} not found")

    def get_all_accounts(self) -> list[AccountModel]:
        return AccountModel.objects.all()

    def create_account(self, owner_name: str, balance: float) -> AccountModel:
        return AccountModel.objects.create(
            owner_name=owner_name,
            balance=balance
        )

    def update_account(
        self,
        account_id: uuid.UUID,
        owner_name: Optional[str] = None,
        balance: Optional[float] = None
    ) -> AccountModel:
        account = self.get_account(account_id)

        if owner_name is not None:
            account.owner_name = owner_name
        if balance is not None:
            account.balance = balance

        account.save()
        return account

    def delete_account(self, account_id: uuid.UUID) -> None:
        account = self.get_account(account_id)
        account.delete()
