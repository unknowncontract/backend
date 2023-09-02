from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from src.routes import image, question, molti
from src.core.container import Container

app = FastAPI(default_response_class=ORJSONResponse)

app.include_router(image.router)
app.include_router(question.router)
app.include_router(molti.router)

container = Container()


@app.get("/")
async def main():
    return ORJSONResponse({"status": 200})
