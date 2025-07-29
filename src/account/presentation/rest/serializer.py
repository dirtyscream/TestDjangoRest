from rest_framework import serializers
from account.infrastructure.database.models import AccountModel


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountModel
        fields = ['id', 'owner_name', 'balance', 'created_at']
        read_only_fields = ['id', 'created_at']
