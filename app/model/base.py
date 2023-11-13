from enum import Enum
from typing import Any

from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    id: Any
    __name__: str

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


class UserSystemRole(str, Enum):
    SUPPER_ADMIN = "SUPPER_ADMIN"
    ADMIN = "ADMIN"
    FARMER = "FARMER"
    SEEDLING_COMPANY = "SEEDLING_COMPANY"
    MANUFACTURER = "MANUFACTURER"
    MEMBER = "MEMBER"


class ProductStatus(str, Enum):
    PUBLISH = "PUBLISH"
    PRIVATE = "PRIVATE"
    CLOSE = "CLOSE"


class ProductType(str, Enum):
    FARMER = "FARMER"
    SEEDLING_COMPANY = "SEEDLING_COMPANY"
    MANUFACTURER = "MANUFACTURER"


class ConfirmStatusUser(str, Enum):
    NONE = "NONE"
    PENDING = "PENDING"
    DONE = "DONE"


class ConfirmUser(str, Enum):
    ACCEPT = "ACCEPT"
    REJECT = "REJECT"


class NotificationType(str, Enum):
    SYSTEM_NOTIFICATION = "SYSTEM_NOTIFICATION"
    PRODUCT_NOTIFICATION = "PRODUCT_NOTIFICATION"
    SEEDLING_COMPANY_NOTIFICATION = "SEEDLING_COMPANY_NOTIFICATION"
    FRAMER_NOTIFICATION = "FRAMER_NOTIFICATION"
    MANUFACTURER_NOTIFICATION = "MANUFACTURER_NOTIFICATION"
    TRANSACTION_NOTIFICATION = "TRANSACTION_NOTIFICATION"
    POST_NOTIFICATION = "POST_NOTIFICATION"
    COMMENT_NOTIFICATION = "COMMENT_NOTIFICATION"


class ActivityType(str, Enum):
    PRODUCT = "PRODUCT"
    SEEDLING_COMPANY = "SEEDLING_COMPANY"
    FARMER = "FARMER"
    MANUFACTURER = "MANUFACTURER"
    STATUS_PRODUCT = "STATUS_PRODUCT"
    TRANSACTION_SF = "TRANSACTION_SF"
    TRANSACTION_FM = "TRANSACTION_FM"
    MARKETPLACE = "MARKETPLACE"
    GROW_UP = "GROW_UP"
    PURCHASE = "PURCHASE"


class TypeTransaction(str, Enum):
    DEPOSIT = "DEPOSIT"
    WITHDRAW = "WITHDRAW"


class FinancialStatus(str, Enum):
    PENDING = "PENDING"
    DONE = "DONE"
    FAIL = "FAIL"


class AmountMoney(str, Enum):
    _50000 = '50000'
    _100000 = '100000'
    _500000 = '500000'
    _1000000 = '1000000'
    _5000000 = '5000000'
    _10000000 = '10000000'
