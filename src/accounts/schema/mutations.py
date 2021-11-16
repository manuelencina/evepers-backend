from graphene import Mutation, ObjectType, String, Boolean, Field
from django.contrib.auth.hashers import make_password

from .types import AccountCreationInput, AccountType
from accounts.models import Account
from profiles.models import SellerProfile


class CreateAccount(Mutation):
    class Arguments:
        account_data = AccountCreationInput(required=True)

    account = Field(AccountType)
    message = String()
    ok = Boolean()

    def mutate(root, info, account_data):

        if Account.objects.filter(email=account_data.email):
            return CreateAccount(message="Email is already registered", ok=False)
        if Account.objects.filter(username=account_data.username):
            return CreateAccount(message="Username is already registered", ok=False)
        if not account_data.password == account_data.repeated_password:
            return CreateAccount(message="Invalid passwords", ok=False)

        new_account = Account.objects.create(
            email=account_data.email,
            username=account_data.username,
            password=make_password(account_data.password)
        )

        SellerProfile.objects.create(
            account=new_account
        )

        return CreateAccount(account=new_account, message='success', ok=True)


class Mutation(ObjectType):
    create_account = CreateAccount.Field()
