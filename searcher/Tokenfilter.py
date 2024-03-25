STOPWORDS = ("is", "was", "to", "the")

def is_token_instance(token):
    return isinstance(token, Token)

class TokenFilter:
    @classmethod
    def filter(cls, token):
        """
        in: sting or janome.tokenizer.Token
        """
        raise NotImplementedError

class StopWordFilter(TokenFilter):
    @classmethod
    def filter(cls,token):
        if isinstance(token, Token):
            if token.surface in STOPWORDS:
                return None
        if token in STOPWORDS:
            return None
        return token