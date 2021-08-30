import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from repository.models import User as UserModel, Item as ItemModel


class User(SQLAlchemyObjectType):
  class Meta:
      model = UserModel
      interface = (relay.Node, )


class UserConnections(relay.Connection):
  class Meta:
    node = User


class Item(SQLAlchemyObjectType):
  class Meta:
    model = ItemModel
    interface = (relay.Node, )


class ItemConnections(relay.Connection):
  class Meta: 
    node = Item


class Query(graphene.ObjectType):
  node = relay.Node.Field()
  all_users = SQLAlchemyConnectionField(UserConnections)
  all_items = SQLAlchemyConnectionField(ItemConnections)


schema = graphene.Schema(query=Query)    