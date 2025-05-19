from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return  {"message": "Hello, my docker and my fully cd/ci!"}

@app.get("/square/{number}")
async def square_number(number: int):
    return {"number": number, "square": number ** 2}
