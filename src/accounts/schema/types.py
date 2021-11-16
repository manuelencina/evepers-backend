from graphene import InputObjectType, String
from graphene_django import DjangoObjectType

from accounts.models import Account


class AccountType(DjangoObjectType):
    class Meta:
        model = Account
        fields = ('id', 'username', 'email')


class AccountCreationInput(InputObjectType):
    email = String(required=True)
    username = String(required=True)
    password = String(required=True)
    repeated_password = String(required=True)
