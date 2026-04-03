from fastapi import FastAPI

from app.interface.api.router.document import router as document_router

app = FastAPI()
app.include_router(document_router)


@app.get("")
def welcome():
    return "Welcome to the worker processing demo!"
