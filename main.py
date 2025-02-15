from fastapi import FastAPI
import api.read.book
import api.read.intern
import api.read.student
import os
from database.utils import execute_triggers, get_db

base_dir = os.path.dirname(os.path.abspath(__file__))
conn = get_db()
execute_triggers(conn, base_dir + '/database/queries/triggers')

app = FastAPI(title="Mini Sistema de Biblioteca")

app.include_router(api.read.book.router)
app.include_router(api.read.intern.router)
app.include_router(api.read.student.router)

@app.get("/")
def root():
    return {"message": "Bem-vindo à API da Biblioteca"}
