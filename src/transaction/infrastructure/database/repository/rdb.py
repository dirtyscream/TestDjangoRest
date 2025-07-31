
from transaction.domain.entity import Transaction
from transaction.infrastructure.database.repository.mapper import TransactionMapper
from transaction.application.interfaces.repositories.repo import ITransactionRepository


class TransactionRepository(ITransactionRepository):
    mapper: TransactionMapper = TransactionMapper()

    def save(self, transaction: Transaction) -> Transaction:
        model = self.mapper.to_model(transaction)
        model.save()
        return self.mapper.to_entity(model)
