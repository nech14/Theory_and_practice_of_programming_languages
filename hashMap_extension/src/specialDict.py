
from src.iloc import Iloc
from src.ploc import Ploc


class SpecialDict(dict):
    def __init__(self):
        super().__init__()
        self.sorted_keys = {}
        self.iloc = Iloc(self)
        self.ploc = Ploc(self)
