# account/domain/exceptions.py
from rest_framework.exceptions import APIException


class AccountNotFoundException(APIException):
    status_code = 404
    default_detail = 'Account not found'
    default_code = 'account_not_found'

    def __init__(self, account_id=None):
        if account_id:
            self.detail = f"Account {account_id} not found"
        super().__init__()


class InsufficientFundsException(APIException):
    status_code = 422
    default_detail = 'Insufficient funds'
    default_code = 'insufficient_funds'

    def __init__(self, available=None, required=None):
        if available is not None and required is not None:
            self.detail = f"Insufficient funds. Available: {available}, required: {required}"
        super().__init__()


class SelfTransferException(APIException):
    status_code = 422
    default_detail = 'Cannot transfer to the same account'
    default_code = 'self_transfer'


class NegativeAmountException(APIException):
    status_code = 422
    default_detail = 'Transfer amount must be positive'
    default_code = 'negative_amount'
