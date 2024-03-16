import strawberry
from fastapi import FastAPI
from strawberry.asgi import GraphQL
from cosine_similarity.application import Similarity


sim = Similarity()

@strawberry.type
class CosineSim:
    value: float

@strawberry.type
class Query:
    @strawberry.field
    def cosinesim(self, v1: int, v2: int) -> CosineSim:
        return CosineSim(value=sim.calculate_similarity(
                str(v1).zfill(3),
                str(v2).zfill(3)
            ))

schema = strawberry.Schema(query=Query)

graphql_app = GraphQL(schema)

app = FastAPI()
app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)
