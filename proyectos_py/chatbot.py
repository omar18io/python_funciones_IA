class Chatbot:
    def __init__(self):
        self._corpus = nltk.corpus.conversatinal.corpus()
    def get_response(self, message):
        # Encuentra las frases más similares al mensaje del usuario.
        most_similar_phrases = self._corpus.most_similar(message)
        # Elige una de las frases más similares como respuesta.
        response = most_similar_phrases[0][0]
        return response