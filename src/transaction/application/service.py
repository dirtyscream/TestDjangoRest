from uuid import UUID
from decimal import Decimal
from transaction.domain.entity import Transaction
from transaction.infrastructure.database.repository.rdb import TransactionRepository
from transaction.application.interfaces.services.service import ITransactionService
from account.infrastructure.database.repository.rdb import AccountRepository
from account.domain.entity import Account
from django.utils import timezone
from django.db import transaction as db_transaction


class TransactionService(ITransactionService):
    transaction_repository = TransactionRepository()
    account_repository = AccountRepository()

    @db_transaction.atomic
    def execute_transfer(self,
                         from_account: UUID,
                         to_account: UUID,
                         amount: Decimal) -> Transaction:
        from_account: Account = self.account_repository.get_by_id(from_account)
        to_account: Account = self.account_repository.get_by_id(to_account)
        from_account.transfer_to(to_account, amount)
        self.account_repository.save(from_account)
        self.account_repository.save(to_account)
        transaction = Transaction(
            id=None,
            from_account=from_account,
            to_account=to_account,
            amount=amount,
            created_at=timezone.now()
        )
        return self.transaction_repository.save(transaction)
