from fastapi import FastAPI
import asyncio
import concurrent.futures
import math
import random

app = FastAPI()

exponential_counter = 0.1  # Initialize the exponential counter
def exponential_function(limit):
    result = 1
    while True:
        yield result
        result *= 2
        if result > limit:
            break

@app.get("/")
def greetings():
    return {"Home Page"}

@app.get("/exponential/{limit}")
async def calculate_exponential(limit: int):
    exp_gen = exponential_function(limit)
    exponential_values = [value for value in exp_gen]
    return {"exponential_values": exponential_values}

@app.get("/exponential_increase")
async def exponential_increase():
    global exponential_counter  # Use the global counter variable

    # Calculate the current exponential value
    current_exponential_value = math.exp(exponential_counter)

    # Increment the counter for the next call
    exponential_counter += 0.1  # You can adjust the increment factor as needed

    return {"exponential_value": current_exponential_value}
    
@app.get("/matrix_multiplication")
async def matrix_multiplication():
    def generate_matrix(rows, cols):
        return [ [random.randint(1, 100) for _ in range(cols)] for _ in range(rows)]

    # Generating the first matrix
    dimension1 = random.randint(100, 200)
    dimension2 = random.randint(100, 200)
    dimension3 = random.randint(100, 200)
    
    matrix1 = generate_matrix(dimension1, dimension2)

    # Generating the second matrix
    matrix2 = generate_matrix(dimension2, dimension3)
    # Example matrices
   
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

@app.get("/calculate/{number}")
async def calculate(number: int):
    loop = asyncio.get_event_loop()

    # Execute the math calculation asynchronously using a thread pool executor
    with concurrent.futures.ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, perform_math_calculation, number)

    return {"result": result}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8888)

# You can test the server by sending a GET request to http://localhost:8000/calculate/{number} where {number} is the integer you want to perform the math calculation on. The server will return a JSON response with the result.
