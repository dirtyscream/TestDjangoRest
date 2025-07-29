class AccountNotFoundException(Exception):
    pass


class InsufficientFundsException(Exception):
    pass


class SelfTransferException(Exception):
    pass


class NegativeAmountException(Exception):
    pass
