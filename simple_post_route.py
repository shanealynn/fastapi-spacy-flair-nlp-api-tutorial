
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define the expected JSON format as a class from Pydantic:
class QueryString(BaseModel):
    """
    This class only contains one element, a string called "query".
    This setup will set Pydantic to expect a dictionary of format:
    {"query": "Some sort of string"}
    """
    query: str


# Add a simple GET response at the base url "/"
@app.get("/")
def read_root():
    return {"test_response": "Hello World!"}


# set up a route that is accessed with POST
@app.post("/analysis/")
def analyse_text(query_string: QueryString):
    return {
        "dataReceived": query_string,
        "success": True,
        }
