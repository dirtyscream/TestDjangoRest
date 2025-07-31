from decimal import DecimalException
from core.presentation.viewsets.base_viewset import BaseViewSet
from core.presentation.mixins.mixins import CreateModelMixin
from transaction.application.service import TransactionService
from transaction.presentation.rest.serializer import TransactionSerializer
from transaction.domain.entity import Transaction
from rest_framework.exceptions import ValidationError


class TransactionViewSet(BaseViewSet,
                         CreateModelMixin):
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
