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
    matrix1 = [[6, 70, 48, 78, 22, 2, 96, 81, 41, 66],
    [57, 7, 71, 30, 13, 39, 9, 60, 31, 68],
    [41, 74, 33, 39, 82, 47, 66, 42, 42, 9],
    [73, 40, 32, 20, 65, 71, 71, 64, 99, 23],
    [25, 14, 17, 9, 38, 61, 58, 74, 31, 27],
    [23, 53, 75, 20, 57, 31, 88, 34, 98, 99],
    [11, 73, 37, 5, 84, 69, 51, 26, 39, 25],
    [40, 48, 15, 32, 15, 54, 100, 18, 8, 11],
    [22, 23, 26, 34, 92, 59, 32, 2, 28, 92],
    [74, 35, 36, 59, 20, 84, 6, 90, 21, 67]
    ]
    
    matrix2 = [
    [11, 47, 35, 18, 36, 74, 9, 25, 35, 43],
    [63, 66, 6, 57, 77, 76, 17, 45, 74, 24],
    [34, 72, 48, 25, 40, 72, 92, 52, 34, 26],
    [25, 17, 89, 90, 43, 77, 88, 66, 27, 64],
    [2, 12, 97, 44, 32, 64, 49, 21, 25, 61],
    [7, 20, 42, 80, 62, 48, 80, 37, 53, 67],
    [63, 66, 65, 44, 84, 50, 56, 4, 73, 41],
    [12, 46, 73, 79, 18, 39, 60, 78, 83, 45],
    [92, 81, 94, 15, 82, 46, 11, 69, 75, 7],
    [43, 21, 69, 51, 58, 9, 5, 97, 73, 84]
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
