# backend/api/routes/graph_routes.py

from fastapi import APIRouter
from services.graph_service import generate_persona_graph

router = APIRouter()

@router.get("/persona")
async def persona_graph(username: str):
    graph = await generate_persona_graph(username)
    return graph
