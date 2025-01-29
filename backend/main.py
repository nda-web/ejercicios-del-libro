from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
import strawberry
from database import engine, Base
from schemas import Query, Mutation

# Crear la base de datos
Base.metadata.create_all(bind=engine)

# Definir el esquema de GraphQL
schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)

# Iniciar FastAPI
app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")

@app.get("/")
def root():
    return {"message": "Servidor FastAPI con GraphQL activo"}
