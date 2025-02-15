from fastapi import FastAPI
import api.read.book, api.read.employee, api.read.intern, api.read.librarian, api.read.loan, api.read.reader, api.read.student, api.read.teacher
import api.update.book, api.update.employee, api.update.intern, api.update.librarian, api.update.loan, api.update.reader, api.update.student, api.update.teacher
import api.create.book, api.create.employee, api.create.intern, api.create.librarian, api.create.loan, api.create.reader, api.create.student, api.create.teacher
import api.delete.book, api.delete.employee, api.delete.intern, api.delete.librarian, api.delete.loan, api.delete.reader, api.delete.student, api.delete.teacher

app = FastAPI(title="Mini Sistema de Biblioteca")

app.include_router(api.read.book.router)
app.include_router(api.read.employee.router)
app.include_router(api.read.intern.router)
app.include_router(api.read.librarian.router)
app.include_router(api.read.student.router)
app.include_router(api.read.student.router)
app.include_router(api.read.student.router)
app.include_router(api.read.student.router)

app.include_router(api.update.student.router)
app.include_router(api.update.student.router)
app.include_router(api.update.student.router)
app.include_router(api.update.student.router)
app.include_router(api.update.student.router)
app.include_router(api.update.student.router)
app.include_router(api.update.student.router)
app.include_router(api.update.student.router)

app.include_router(api.create.student.router)
app.include_router(api.create.student.router)
app.include_router(api.create.student.router)
app.include_router(api.create.student.router)
app.include_router(api.create.student.router)
app.include_router(api.create.student.router)
app.include_router(api.create.student.router)
app.include_router(api.create.student.router)

app.include_router(api.delete.student.router)
app.include_router(api.delete.student.router)
app.include_router(api.delete.student.router)
app.include_router(api.delete.student.router)
app.include_router(api.delete.student.router)
app.include_router(api.delete.student.router)
app.include_router(api.delete.student.router)
app.include_router(api.delete.student.router)


@app.get("/")
def root():
    return {"message": "Bem-vindo à API da Biblioteca"}
