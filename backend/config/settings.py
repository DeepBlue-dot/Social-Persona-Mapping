from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    NEO4J_URI: str = "bolt://localhost:7687"
    NEO4J_USER: str = "neo4j"
    NEO4J_PASSWORD: str = "password"
    JWT_SECRET: str = "change-this"
    JWT_ALGORITHM: str = "HS256"

    model_config = {
        "env_file": ".env",
        "extra": "ignore"
    }

settings = Settings()
