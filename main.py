from fastapi import FastAPI
import api.read.book
import api.read.intern
import api.read.student

app = FastAPI(title="Mini Sistema de Biblioteca")

app.include_router(api.read.book.router)
app.include_router(api.read.intern.router)
app.include_router(api.read.student.router)

@app.get("/")
def root():
    return {"message": "Bem-vindo à API da Biblioteca"}
