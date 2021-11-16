from graphene import ObjectType, String, Schema

from accounts.schema.mutations import Mutation as AccountMutation
from accounts.schema.queries import Query as AccountQuery


class Query(
    AccountQuery,
    ObjectType
):
    pass


class Mutation(
    AccountMutation,
    ObjectType
):
    pass


schema = Schema(query=Query, mutation=Mutation)
