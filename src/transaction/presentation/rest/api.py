from decimal import DecimalException
from core.presentation.viewsets.base_viewset import BaseViewSet
from core.presentation.mixins.mixins import CreateModelMixin, ListModelMixin
from transaction.application.service import TransactionService
from transaction.presentation.rest.serializer import TransactionSerializer
from transaction.domain.entity import Transaction
from rest_framework.exceptions import ValidationError


class TransactionViewSet(BaseViewSet,
                         CreateModelMixin,
                         ListModelMixin):
    serializer_class = TransactionSerializer
    service = TransactionService()

    def create_entity(self, data) -> Transaction:
        try:
            return self.service.execute_transfer(
                from_account=data['from_account']['id'],
                to_account=data['to_account']['id'],
                amount=data['amount']
            )
        except (KeyError, ValueError, DecimalException) as e:
            raise ValidationError(detail=f"Invalid input: {str(e)}")

    def get_all_entities(self, params: dict | None = None):
        if params and 'account_id' in params:
            return self.service.get_for_account(params['account_id'])
        raise ValidationError(
            detail=f"Invalid input, try to filter by account id",)
