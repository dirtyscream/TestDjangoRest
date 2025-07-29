class AccountNotFoundException(Exception):
    """Exception raised when a blog post is not found."""
    pass


class AccountValidationError(Exception):
    """Exception raised for errors in the input data during blog post operations."""
    pass
