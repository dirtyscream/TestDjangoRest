from typing import Optional
import uuid
from account.infrastructure.database.models import AccountModel
from account.domain.entity import Account
from account.domain.exception import AccountNotFoundException


class AccountService:
    def get_account(self, account_id: uuid.UUID) -> Account:
        try:
            model = AccountModel.objects.get(id=account_id)
            return self._to_entity(model)
        except AccountModel.DoesNotExist:
            raise AccountNotFoundException(f"Account {account_id} not found")

    def get_all_accounts(self) -> list[Account]:
        return [self._to_entity(model) for model in AccountModel.objects.all()]

    def create_account(self, owner_name: str, balance: float) -> Account:
        model = AccountModel.objects.create(
            owner_name=owner_name,
            balance=balance
        )
        return self._to_entity(model)

    def update_account(
        self,
        account_id: uuid.UUID,
        owner_name: Optional[str] = None,
        balance: Optional[float] = None
    ) -> Account:
        model = AccountModel.objects.get(id=account_id)

        if owner_name is not None:
            model.owner_name = owner_name
        if balance is not None:
            model.balance = balance

        model.save()
        return self._to_entity(model)

    def delete_account(self, account_id: uuid.UUID) -> None:
        model = AccountModel.objects.get(id=account_id)
        model.delete()

    def transfer_funds(
        self,
        from_account_id: uuid.UUID,
        to_account_id: uuid.UUID,
        amount: float
    ) -> None:
        from_account = self.get_account(from_account_id)
        to_account = self.get_account(to_account_id)
        from_account.transfer_to(to_account, amount)
        AccountModel.objects.filter(id=from_account.id).update(
            balance=from_account.balance)
        AccountModel.objects.filter(id=to_account.id).update(
            balance=to_account.balance)

    @staticmethod
    def _to_entity(model: AccountModel) -> Account:
        return Account(
            id=model.id,
            owner_name=model.owner_name,
            balance=model.balance
        )
