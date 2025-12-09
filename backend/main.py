from fastapi import FastAPI

app = FastAPI(
    title="Social Persona Mapping API",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"status": "API running"}
