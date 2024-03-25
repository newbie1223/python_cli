import MeCab


class Analyzer:
    tokenizer = None
    char_filters = []
    token_filters = []

    @classmethod
    def analyze(cls, text: str):
        text = cls._char_filter(text)
        tokens = cls.tokenizer.tokenize(text)
        filtered_token = (cls._token_filter(token) for token in tokens)
        return [parse_token(t) for t in filtered_token if t]

    @classmethod
    def _char_filter(cls, text):
        for char_filter in cls.char_filters:
            text = char_filter.filter(text)
        return text
    
    @classmethod
    def _token_filter(cls, token):
        for token_filter in cls.token_filters:
            token = token_filter.filter(token)
        return token

class JapaneseAnalyzer(Analyzer):
    tokenizer = MecabTokenizerTokenizer
    char_filters = [LowercaseFilter]
    token_filters = [StopWordFilter]

class EnglishAnalyzer(Analyzer):
    tokenizer = WhitespaceTokenizerTokenizer
    char_filters = [LowercaseFilter]
    token_filters = [StopWordFilter]