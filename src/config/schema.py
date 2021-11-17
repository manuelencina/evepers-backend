from graphene import ObjectType, String, Schema
import graphql_jwt

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
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    delete_token_cookie = graphql_jwt.DeleteJSONWebTokenCookie.Field()
    delete_refresh_token_cookie = graphql_jwt.DeleteRefreshTokenCookie.Field()


schema = Schema(query=Query, mutation=Mutation)
