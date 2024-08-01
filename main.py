import uvicorn
import subprocess

from fastapi import FastAPI

from app.core.logger import logger
from app.db.schemas import HelloWorldInput, HelloWorldOutput

app = FastAPI()

logger.info("Application start-up successful!")


@app.post("/hello-world/", response_model=HelloWorldOutput)
def hello_world(input: HelloWorldInput):
    logger.info("Called end-point ")
    response = HelloWorldOutput(text=input.text)
    return response


if __name__ == "__main__":
    subprocess.run("pytest")
    uvicorn.run("main:app", reload=True)
