# transaction/presentation/rest/serializer.py
from rest_framework import serializers
from transaction.infrastructure.database.models import TransactionModel


class TransactionSerializer(serializers.ModelSerializer):
    from_account = serializers.UUIDField(source='from_account.id')
    to_account = serializers.UUIDField(source='to_account.id')

    class Meta:
        model = TransactionModel
        fields = ['id', 'from_account', 'to_account', 'amount', 'created_at']
        read_only_fields = ['id', 'created_at']
        extra_kwargs = {
            'amount': {'required': True, 'min_value': 0.00001}
        }
