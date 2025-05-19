from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.get("/square/{number}")
async def square_number(number: int):
    return {"number": number, "square": number ** 2}
