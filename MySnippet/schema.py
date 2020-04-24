import graphene
# import snippets.schema.Query
from snippets.schema import Query as snippets_query

class Query(snippets_query):
    pass

schema = graphene.Schema(query=Query)
