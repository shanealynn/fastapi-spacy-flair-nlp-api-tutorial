from pydantic import BaseModel
from fastapi import FastAPI
from get_entities_and_sentment import get_entities_and_sentiment

app = FastAPI()


class QueryString(BaseModel):
    query: str


@app.get("/")
def read_root():
    return {"test_response": "The API is working!"}


@app.post("/analysis/")
def analyse_text(query_string: QueryString):

    sentiment, entities = get_entities_and_sentiment(query_string.query)
    return {
        "query": query_string.query,
        "entites": entities,
        "sentiment": sentiment,
        }
