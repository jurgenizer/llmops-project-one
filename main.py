from fastapi import FastAPI

# Create an app which is the FastAPI object
app = FastAPI()

# HTTP Methods (GET, POST, PUT, DELETE)

# GET
@app.get("/")
def welcome():
    return {"message": "Hello world"}

@app.get("/home")
def welcome():
    return {"message": "Welcome home"}

# POST
@app.post("/dummy")
def demo_function(data):
    return {"message": data}