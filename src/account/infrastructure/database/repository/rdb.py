from account.domain.entity import BlogPost
from account.infrastructure.database.models import AccountModel
from account.infrastructure.database.repository.mapper import AccountMapper


class AccountRepository:
    def __init__(self, model_mapper: AccountMapper):
        self.model_mapper = model_mapper

    def save(self, entity: BlogPost) -> BlogPost:
        instance: AccountModel = self.model_mapper.to_instance(entity=entity)
        instance.save()
        return self.model_mapper.to_entity(instance=instance)

    def get_by_id(self, id: int) -> BlogPost:
        instance = AccountModel.objects.get(id=id)
        return self.model_mapper.to_entity(instance=instance)

    def delete(self, id: int):
        AccountModel.objects.filter(id=id).delete()

    def list_all(self) -> list[BlogPost]:
        instances = AccountModel.objects.all()
        return self.model_mapper.to_entity_list(instances=instances)
