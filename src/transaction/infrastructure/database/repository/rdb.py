from decimal import Decimal
from typing import List
from uuid import UUID
from django.db import transaction as db_transaction
from transaction.infrastructure.database.models import TransactionModel
from transaction.domain.entity import Transaction
from transaction.infrastructure.database.repository.mapper import TransactionMapper
from django.utils import timezone
from account.infrastructure.database.repository.rdb import AccountRepository
from transaction.domain.exception import TransactionNotFoundException


class TransactionRepository:
    def __init__(self, mapper: TransactionMapper):
        self.mapper = TransactionMapper()

    def save(self, transaction: Transaction) -> Transaction:
        with db_transaction.atomic():
            model = self.mapper.to_model(transaction)
            model.save()
            return self.mapper.to_entity(model)

    def get_by_id(self, transaction_id: UUID) -> Transaction:
        try:
            model = TransactionModel.objects.get(id=transaction_id)
            return self.mapper.to_entity(model)
        except TransactionModel.DoesNotExist:
            raise TransactionNotFoundException(
                f"Transaction {transaction_id} not found")

    def get_all_for_account(self, account_id: UUID) -> List[Transaction]:
        models = TransactionModel.objects.filter(
            models.Q(from_account_id=account_id) |
            models.Q(to_account_id=account_id)
        ).order_by('-created_at')
        return self.mapper.to_entity_list(models)

    @db_transaction.atomic
    def execute_transfer(
        self,
        from_account_id: UUID,
        to_account_id: UUID,
        amount: Decimal
    ) -> Transaction:
        transaction = Transaction(
            id=None,
            from_account=AccountRepository.get_by_id(from_account_id),
            to_account=AccountRepository.get_by_id(to_account_id),
            amount=amount,
            created_at=timezone.now()
        )
        return self.save(transaction)
