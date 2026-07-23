import spacy

nlp = spacy.load("en_core_web_sm")


class EntityExtractor:

    def extract(self, text: str):

        doc = nlp(text)

        entities = []

        for entity in doc.ents:

            entities.append({
                "text": entity.text,
                "label": entity.label_
            })

        return entities