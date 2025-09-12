from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_roo():
    return {"message": "Welcome to  backend!"}
