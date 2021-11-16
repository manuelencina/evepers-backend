from graphene import ObjectType, String, Field, ID

from .types import AccountType
from accounts.models import Account


class Query(ObjectType):
    profile = Field(AccountType)

    def resolve_profile(root, info):
        current_account_id = info.context.user.id
        current_account = Account.objects.get(pk=current_account_id)

        return current_account
