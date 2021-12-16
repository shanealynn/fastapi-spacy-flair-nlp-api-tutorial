# FastAPI NLP API - Sentiment Analysis and Entity Detection API

Accompanying code to www.shanelynn.ie tutorial on FastAPI NLP API creation. 

In this simple API, we're building a web application that can process text in HTTP requests to extract sentiment and entities automatically.

## Installation

Start a virtual environment (`python3 -m venv venv`) and install the requirements in that virtual environment (FastAPI, Spacy, Flair, Uvicorn[standard]). This tutorial was built with Python 3.9 originally. 

`pip install -r requirements.txt`

You'll also need to install language models for Spacy:

`python -m spacy download en_core_web_sm`


## Running the main API

Start the main API with:

`uvicorn simple_api:app --reload`

The first run may take longer than usual if Flair has to download any models to run.

## Examples

There are some basic examples (from the blog) in the `examples/` directory showing:

* Basic GET requests with FastAPI `simple_api.py`
* Basic POST API with FastAPI `simple_post_route.py`
* Sentiment detection with Flair alone `flair_sentiment_sample.py`
* Named entity recognition (NER) with Spacy `spacy_ner_example.py`


Run these with simple `python examples/<example_filename.py>`.

## Testing with cURL

You can test the application with curl commands. Send a request with the text of your choosing to http://localhost:8000 when the API is running.

`curl -X POST -H "Content-Type: application/json" -d '{"query": "I absolutely love building Python applications with FastAPI and Shane's blog."}' http://localhost:8000/analysis/`
