from fastapi import FastAPI

app = FastAPI()


@app.get("/data")
async def root():
    return {"message": "Hello devops"}