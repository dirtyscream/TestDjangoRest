from typing import List, TypeVar

from django.db.models import Model
from account.domain.entity import Account
from account.infrastructure.database.models import AccountModel
DjangoModelType = TypeVar("DjangoModelType", bound=Model)


class AccountMapper:
    def to_entity(self, instance: AccountModel) -> Account:
        return Account(
            id=instance.id,
            owner_name=instance.owner_name,
            balance=float(instance.balance),
            created_at=instance.created_at,
        )

    def to_model(self, entity: Account) -> AccountModel:
        return AccountModel(
            id=entity.id,
            owner_name=entity.owner_name,
            balance=entity.balance,
            created_at=entity.created_at,
        )

    def to_entity_list(self, instances: List[AccountModel]) -> List[Account]:
        return [self.to_entity(instance=i) for i in instances]

    def to_instance_list(self, entities: List[Account]) -> List[AccountModel]:
        return [self.to_model(entity=e) for e in entities]
