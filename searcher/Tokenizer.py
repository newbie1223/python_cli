import MeCab

tokenizer = Tokenizer()

class BaseTokenizer:
    @classmethod
    def tokenize(cls, text):
        raise NotImplementedError
    # def tokenizer(text):
    #     t = MeCab.Tagger("")
    #     t.parse("")
    #     m = t.parseToNode(text)
    #     tokens = []
    #     while m:
    #         tokenData = m.feature.split(",")
    #         token = [m.surface]
    #         for data in tokenData:
    #             token.append(data)
    #         tokens.append(token)
    #         m = m.next
    #     tokens.pop(0)
    #     tokens.pop(-1)
    #     return tokens

class MecabTokenizer(BaseTokenizer):
    @classmethod
    def tokenize(cls, text):
        return(t for t in cls.tokenizer.tokenize(text))

class WhitespaceTokenizer(BaseTokenizer):
    @classmethod
    def tokenize(cls, text):
        return (t[0] for t in re.finditer(r"[^ \t\r\n]+", text))