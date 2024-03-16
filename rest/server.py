from fastapi import FastAPI
from cosine_similarity.application import Similarity

app = FastAPI()
sim = Similarity()


@app.get("/")
async def root(v1: str, v2: str):
    return {"cosine_sim": sim.calculate_similarity(v1, v2)}
