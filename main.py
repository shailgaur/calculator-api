
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Literal

app = FastAPI()


# Home endpoint
@app.get("/")
def home():
    return {"message": "Calculator API is running - CI/CD demo"}


# Existing addition endpoint
@app.get("/add")
def add(a: float, b: float):
    return {"result": a + b}


# Define JSON request structure
class CalculatorRequest(BaseModel):
    number1: float
    number2: float
    operation: Literal["add", "subtract", "multiply", "divide"]


# POST endpoint
@app.post("/calculate")
def calculate(request: CalculatorRequest):

    if request.operation == "add":
        result = request.number1 + request.number2

    elif request.operation == "subtract":
        result = request.number1 - request.number2

    elif request.operation == "multiply":
        result = request.number1 * request.number2

    elif request.operation == "divide":
        if request.number2 == 0:
            raise HTTPException(
                status_code=400,
                detail="Cannot divide by zero"
            )
        result = request.number1 / request.number2

    return {
        "number1": request.number1,
        "number2": request.number2,
        "operation": request.operation,
        "result": result
    }



