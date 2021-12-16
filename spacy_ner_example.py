"""
A simple example showing Named-Entity Recognition (NER) with the Spacy
library in Python.

Shane Lynn 2021
"""

import spacy
nlp = spacy.load("en_core_web_sm")

# Here is a sample sentence with some entities:
sample_text = "I was walking down 5th Avenue yesterday in New York City and I saw Bill Gates!"

# For Spacy, first turn your raw text data into a "document":
doc = nlp(sample_text)
# The document then "magically" has everything calculated:
for entity in doc.ents:
    print(f"Entity Detected: {entity.text}, of type: {entity.label_}")
