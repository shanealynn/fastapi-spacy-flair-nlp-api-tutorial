from typing import Tuple, List

from typing import Tuple, List
from flair.models import TextClassifier
from flair.data import Sentence
import spacy

nlp = spacy.load("en_core_web_sm")
sentiment_model = TextClassifier.load('en-sentiment')


def get_entities_and_sentiment(text: str) -> Tuple[dict, List[dict]]:
    """Parse a string, and determine sentiment polarity and entities contained within"""
    doc = nlp(text)
    entity_list = [
        {"name": x.text, "type": x.label_} for x in doc.ents
    ]
    sentence = Sentence(text)
    sentiment_model.predict(sentence)
    label = sentence.labels[0]
    sentiment = {'sentiment': label.value, 'polarity': label.score}
    return sentiment, entity_list


# Run a small test
if __name__ == '__main__':
    # We're testing if our sentiment and entity function is working correctly:
    result = get_entities_and_sentiment("I travelled to New York and I hated it.")
    print(result)
