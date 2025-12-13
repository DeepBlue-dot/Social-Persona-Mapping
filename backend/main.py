# backend/main.py

from fastapi import FastAPI
from api.routes.osint_routes import router as osint_router
from api.routes.analysis_routes import router as analysis_router
from api.routes.graph_routes import router as graph_router
from api.routes.auth_routes import router as auth_router

app = FastAPI(
    title="Social Persona Mapping OSINT API",
    version="1.0.0",
)

# Register routes
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(osint_router, prefix="/osint", tags=["Data Collection"])
app.include_router(analysis_router, prefix="/analysis", tags=["Analysis"])
app.include_router(graph_router, prefix="/graph", tags=["Graph & Network"])
