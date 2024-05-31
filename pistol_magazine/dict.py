from pistol_magazine.base import _BaseField


class Dict(_BaseField):

    def __init__(self, dict_fields: dict = None):
        from pistol_magazine.int import Int
        from pistol_magazine.str import Str
        from pistol_magazine.timestamp import Timestamp
        if dict_fields is None:
            self.dict_fields = {"a": Int(), "b": Str(), "c": Timestamp()}
        else:
            self.dict_fields = dict_fields

    def mock(self):
        return {key: value.mock() for key, value in self.dict_fields.items()}

    def to_str(self):
        return {key: value.to_str() for key, value in self.dict_fields.items()}
