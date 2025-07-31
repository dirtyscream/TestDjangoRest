from django.db import models
from django.utils import timezone
import uuid
from account.infrastructure.database.models import AccountModel


class TransactionModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    from_account = models.ForeignKey(
        AccountModel,
        on_delete=models.PROTECT,
        related_name='outgoing_transactions'
    )
    to_account = models.ForeignKey(
        AccountModel,
        on_delete=models.PROTECT,
        related_name='incoming_transactions'
    )
    amount = models.DecimalField(max_digits=15, decimal_places=5)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'transactions'
        indexes = [
            models.Index(fields=['from_account']),
            models.Index(fields=['to_account']),
            models.Index(fields=['created_at']),
        ]
