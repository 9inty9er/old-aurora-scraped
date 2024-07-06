import spacy

nlp = spacy.load('en_core_web_sm')

def process_message(message):
    doc = nlp(message)
    intents = [token.lemma_ for token in doc if token.pos_ == 'VERB']
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return {'intents': intents, 'entities': entities}

