from uuid import UUID
from typing import List
from decimal import Decimal
from transaction.domain.entity import Transaction
from transaction.domain.exception import TransactionNotFoundException
from transaction.infrastructure.database.models import TransactionModel
from transaction.infrastructure.database.repository.rdb import TranscationRepository
from django.utils import timezone


class TranscationService:
    repository = TranscationRepository()

    def get_transaction(self, transaction_id: UUID) -> Transaction:
        try:
            return self.repository.get_by_id(transaction_id)
        except TransactionModel.DoesNotExist:
            raise TransactionNotFoundException(
                f"Transaction {transaction_id} not found")

    def get_all_for_account(self, account_id: UUID) -> List[Transaction]:
        return self.repository.get_all_for_account(account_id)

    def execute_transfer(self,
                         from_account: UUID,
                         to_account: UUID,
                         amount: Decimal) -> Transaction:
        return self.repository.execute_transfer(from_account, to_account, amount)
