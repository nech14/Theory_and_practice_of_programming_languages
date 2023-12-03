class IlocException(Exception):
    pass


class Iloc(dict):
    def __init__(self, d: dict):
        super().__init__()
        self.d = d

    def __getitem__(self, index: int):
        if 0 <= index < len(self.d):
            self.d = {x: y for x, y in sorted(self.d.items())}
            return self.d[list(self.d.keys())[index]]

        raise IlocException("Invalid index")
