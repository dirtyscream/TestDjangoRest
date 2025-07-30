from injector import inject
from core.application.viewsets.base_viewset import BaseModelViewSet
from account.application.service import AccountService
from account.presentation.rest.serializer import AccountSerializer


class AccountViewSet(BaseModelViewSet):
    serializer_class = AccountSerializer

    @inject
    def __init__(self, service: AccountService, **kwargs):
        self.service = service
        super().__init__(**kwargs)

    def get_entity(self, entity_id: str):
        return self.service.get_account(entity_id)

    def get_all_entities(self):
        return self.service.get_all_accounts()

    def create_entity(self, data: dict):
        return self.service.create_account(
            owner_name=data['owner_name'],
            balance=data['balance']
        )
