from typing import List
from django.db.models import Q
from account.domain.entity import Account
from transaction.domain.entity import Transaction
from transaction.infrastructure.database.repository.mapper import TransactionMapper
from transaction.application.interfaces.repositories.repo import ITransactionRepository
from transaction.infrastructure.database.models import TransactionModel


class TransactionRepository(ITransactionRepository):
    mapper: TransactionMapper = TransactionMapper()

    def save(self, transaction: Transaction) -> Transaction:
        model = self.mapper.to_model(transaction)
        model.save()
        return self.mapper.to_entity(model)

    def get_for_account(self, account: Account) -> List[Transaction]:
        qs = TransactionModel.objects.filter(
            Q(from_account_id=account.id) | Q(to_account_id=account.id)
        ).order_by('-created_at')
        return self.mapper.to_entity_list(qs)
