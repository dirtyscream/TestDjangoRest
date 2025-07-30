from django.db import models
from django.utils import timezone
import uuid


class AccountModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner_name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=5)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        app_label = 'account'
