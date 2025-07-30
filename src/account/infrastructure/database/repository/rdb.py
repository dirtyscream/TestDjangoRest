from uuid import UUID
from typing import List
from account.domain.entity import Account
from account.infrastructure.database.models import AccountModel
from account.infrastructure.database.repository.mapper import AccountMapper


class AccountRepository:
    def __init__(self, mapper: AccountMapper):
        self.mapper = mapper

    def save(self, entity: Account) -> Account:
        model = self.mapper.to_model(entity)
        model.save()
        return self.mapper.to_entity(model)

    def get_by_id(self, id: UUID) -> Account:
        try:
            model = AccountModel.objects.get(id=id)
            return self.mapper.to_entity(model)
        except AccountModel.DoesNotExist:
            raise

    def list_all(self) -> List[Account]:
        models = AccountModel.objects.all()
        return self.mapper.to_entity_list(models)
