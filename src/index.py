from fastapi import FastAPI
import asyncio
import concurrent.futures
import math

app = FastAPI()

@app.get("/")
def greetings():
    return {"Home Page"}

@app.get("/matrix_multiplication")
async def matrix_multiplication():
    # Example matrices
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
    ]

    matrix2 = [
        [7, 8],
        [9, 10],
        [11, 12],
    ]
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Matrices cannot be multiplied. Inner dimensions must match.")

    result = [[0 for i in range(len(matrix2[0]))] for j in range(len(matrix1))]

    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    print(result)
    
    for row in result:
        print(row)
    
    return result
    
def perform_math_calculation(number):
    t = number

    art = math.tan(t)
    atan_art = math.atan(art)
    atan2_t_art = math.atan2(t, art)
    atan2_art_t = math.atan2(art, t)

    return {
        "art": art,
        "atan_art": atan_art,
        "atan2_t_art": atan2_t_art,
        "atan2_art_t": atan2_art_t
    }

@app.get("/calculate")
async def calculate(number: int):
    loop = asyncio.get_event_loop()

    # Execute the math calculation asynchronously using a thread pool executor
    with concurrent.futures.ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, perform_math_calculation, number)

    return {"result": result}
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

# You can test the server by sending a GET request to http://localhost:8000/calculate/{number} where {number} is the integer you want to perform the math calculation on. The server will return a JSON response with the result.
