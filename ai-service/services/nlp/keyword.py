import spacy

nlp = spacy.load("en_core_web_sm")


class KeywordExtractor:

    def extract(self, text: str):

        doc = nlp(text)

        keywords = []

        for token in doc:

            if token.is_alpha and not token.is_stop:

                keywords.append(token.lemma_.lower())

        return sorted(list(set(keywords)))