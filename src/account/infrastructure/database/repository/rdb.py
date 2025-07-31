from uuid import UUID
from typing import List
from account.domain.entity import Account
from account.infrastructure.database.models import AccountModel
from account.infrastructure.database.repository.mapper import AccountMapper


class AccountRepository:
    mapper = AccountMapper()

    def save(self, entity: Account) -> Account:
        if entity.id is None:
            return self._create(entity)
        return self._update(entity)

    def _create(self, entity: Account) -> Account:
        model = self.mapper.to_model(entity)
        model.save()
        return self.mapper.to_entity(model)

    def _update(self, entity: Account) -> Account:
        try:
            model = AccountModel.objects.get(id=entity.id)
            model.owner_name = entity.owner_name
            model.balance = entity.balance
            model.save()
            return self.mapper.to_entity(model)
        except AccountModel.DoesNotExist:
            raise ValueError(f"Account with id {entity.id} does not exist")

    def get_by_id(self, id: UUID) -> Account:
        try:
            model = AccountModel.objects.get(id=id)
            return self.mapper.to_entity(model)
        except AccountModel.DoesNotExist:
            raise

    def list_all(self) -> List[Account]:
        models = AccountModel.objects.all()
        return self.mapper.to_entity_list(models)
