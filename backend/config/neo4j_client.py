# backend/config/neo4j_client.py

from neo4j import GraphDatabase
from .settings import settings

driver = GraphDatabase.driver(
    settings.NEO4J_URI,
    auth=(settings.NEO4J_USER, settings.NEO4J_PASSWORD),
)

def get_db():
    try:
        yield driver.session()
    finally:
        driver.close()
