from fastapi import FastAPI
import os
from database.utils import get_db
from database.services.database import DataBaseService

base_dir = os.path.dirname(os.path.abspath(__file__))
conn = get_db()
#execute_triggers(conn, base_dir + '/database/queries/triggers')

db = DataBaseService(conn)
db.create()

app = FastAPI(title="Mini Sistema de Biblioteca")

# Inclusão dinâmica das rotas de cada categoria

for action in ["create", "read", "update", "delete"]:
    for entity in ["book", "employee", "loan", "reader"]:
        module = f"api.{action}.{entity}"
        router = __import__(module, fromlist=['router'])
        app.include_router(router.router)

from api.read.book import get_book, get_book_all

@app.get("/", tags=["Root"])
def home():
    print(get_book_all())
    return {"message": "Bem-vindo à API da Biblioteca"}
