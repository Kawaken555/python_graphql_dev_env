from typing import List

from fastapi import Depends, FastAPI, HTTPException
from fastapi.param_functions import Query
from sqlalchemy import schema
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException

from starlette.graphql import GraphQLApp
from graphqlshema import schemas as graphql_schemas
from repository import crud, models, schemas
from repository.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_route("/graphql", GraphQLApp(schema=graphql_schemas.schema))


@app.on_event("shutdown")
def shutdown_event():
    SessionLocal.remove()
