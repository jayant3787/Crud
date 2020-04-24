import graphene
from graphene_django.types import DjangoObjectType
from .models import Snippet
from datetime import datetime

class SnippetType(DjangoObjectType):
    class Meta:
        model = Snippet

class Query(graphene.ObjectType):
    all_snippets = graphene.List(SnippetType)
    user = Snippet(name="jayant", stream="mca", login_time=datetime.now())
    user.save()
    user.name="shashank"
    user.save()
    user.delete()
    user.save()
    user.stream="B TECH"
    user.save()
    def resolve_all_snippets(self, info, **kwargs):
        return Snippet.objects.all()

class CreateSnippet(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        stream = graphene.String()
    user = graphene.Field(Snippet)
   
    def mutate (self, info, **kwargs):
        user = Snippet(name="jayant", stream="mca", login_time=datetime.now())
        user.save()
        user.name="shashank"
        user.save()
        user.delete()
        user.save()
        user.stream="B TECH"
        user.save()
        user.delete(id=153)
        return CreateSnippet.objects.all()
         

class Mutations(graphene.ObjectType):
    create_snippet = CreateSnippet.Field()

