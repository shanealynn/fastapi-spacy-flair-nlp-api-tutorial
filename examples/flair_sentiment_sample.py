"""
A simple demonstration of sentiment analysis using the Python Flair
library.

Shane Lynn 2021
"""

from flair.models import TextClassifier
from flair.data import Sentence

# For Flair, you load models in advance.
# Note that this is memory intensive and can take some time
sentiment_model = TextClassifier.load("en-sentiment")

# We're going to analyse these two texts for sentiment
sample_text = [
    "I love using Python to make really fast APIs.",
    "I hate silly bugs that happen and annoy me."
]

# Simply iterate through the samples, and run the prediction
for text in sample_text:
    # For Flair, you convert your raw data into "sentences" prior to analysis
    sentence = Sentence(text)
    # This is the analysis step, note that it edits the sentence to include the
    # prediction
    sentiment_model.predict(sentence)
    print(f"The sentence '{text}' is detected as {sentence.labels[0]}.")
