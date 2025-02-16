from fastapi import FastAPI
import os
from database.utils import execute_triggers, get_db

base_dir = os.path.dirname(os.path.abspath(__file__))
conn = get_db()
execute_triggers(conn, base_dir + '/database/queries/triggers')

app = FastAPI(title="Mini Sistema de Biblioteca")

# Inclusão dinâmica das rotas de cada categoria
for action in ["create", "read", "update", "delete"]:
    for entity in ["book", "employee", "loan", "reader"]:
        module = f"api.{action}.{entity}"
        router = __import__(module, fromlist=['router'])
        app.include_router(router.router)

@app.get("/")
def root():
    return {"message": "Bem-vindo à API da Biblioteca"}
