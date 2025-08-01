from decimal import Decimal
from uuid import UUID
from typing import List, Optional
from django.db import transaction
from django.db.models import F
from account.domain.entity import Account
from account.infrastructure.database.models import AccountModel
from account.infrastructure.database.repository.mapper import AccountMapper
from account.application.interfaces.repositories.repo import IAccountRepository


class AccountRepository(IAccountRepository):
    mapper = AccountMapper()

    @transaction.atomic
    def save(self, entity: Account) -> Account:
        if entity.id is None:
            return self._create(entity)
        return self._update(entity)

    def _create(self, entity: Account) -> Account:
        model = self.mapper.to_model(entity)
        model.save(force_insert=True)
        return self.mapper.to_entity(model)

    @transaction.atomic
    def _update(self, entity: Account) -> Account:
        try:
            model = AccountModel.objects.select_for_update().get(id=entity.id)
            model.owner_name = entity.owner_name
            model.balance = entity.balance
            model.save()
            return self.mapper.to_entity(model)
        except AccountModel.DoesNotExist:
            raise ValueError(f"Account with id {entity.id} does not exist")

    def get_by_id(self, id: UUID, lock: bool = False) -> Account:
        try:
            qs = AccountModel.objects
            if lock:
                qs = qs.select_for_update()
            model = qs.get(id=id)
            return self.mapper.to_entity(model)
        except AccountModel.DoesNotExist:
            raise

    def list_all(self, limit: Optional[int] = None) -> List[Account]:
        qs = AccountModel.objects.all()
        if limit:
            qs = qs[:limit]
        return self.mapper.to_entity_list(qs)
