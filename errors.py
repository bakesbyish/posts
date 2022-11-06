"""Handle common exceptions."""


class InvalidTitleException(Exception):
    """Handle invalidly long title names for products."""

    def __init__(self, message="Invalid title"):
        """Execute."""
        super(InvalidTitleException, self).__init__(message)


class InvalidSkuException(Exception):
    """Handle invalid chars for sku number."""

    def __init__(self, message="Inavlid sku"):
        """Execute."""
        super(InvalidSkuException, self).__init__(message)


class InvalidPriceException(Exception):
    """Handle invalid chars for price number."""

    def __init__(self, message="Inavalid price"):
        """Execute."""
        super(InvalidPriceException, self).__init__(message)
