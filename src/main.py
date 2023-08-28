from fastapi import FastAPI
from src.routes import image

app = FastAPI()

app.include_router(image.router)


@app.get("/")
async def main():
    return "root"
