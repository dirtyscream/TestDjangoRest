from typing import List
from transaction.domain.entity import Transaction
from transaction.infrastructure.database.models import TransactionModel
from account.infrastructure.database.repository.mapper import AccountMapper


class TransactionMapper:

    def to_entity(self, model: TransactionModel) -> Transaction:
        account_mapper = AccountMapper()
        return Transaction(
            id=model.id,
            from_account=account_mapper.to_entity(model.from_account),
            to_account=account_mapper.to_entity(model.to_account),
            amount=model.amount,
            created_at=model.created_at
        )

    def to_model(self, entity: Transaction) -> TransactionModel:
        account_mapper = AccountMapper()
        return TransactionModel(
            id=entity.id,
            from_account=account_mapper.to_model(entity.from_account),
            to_account=account_mapper.to_model(entity.to_account),
            amount=entity.amount,
            created_at=entity.created_at
        )

    def to_entity_list(self, instances: List[TransactionModel]) -> List[Transaction]:
        return [self.to_entity(instance=i) for i in instances]
