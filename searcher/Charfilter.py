class CharacterFilter:
    @classmethod
    def filter(cls,text: str):
        raise NotImplementedError

class LowercaseFilter(CharacterFilter):
    @classmethod
    def filter(cls, text: str):
        return text.lower()