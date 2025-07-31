
from transaction.domain.entity import Transaction
from transaction.infrastructure.database.repository.mapper import TransactionMapper


class TransactionRepository:
    mapper: TransactionMapper = TransactionMapper()

    def save(self, transaction: Transaction) -> Transaction:
        model = self.mapper.to_model(transaction)
        model.save()
        return self.mapper.to_entity(model)
