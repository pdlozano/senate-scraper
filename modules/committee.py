class Committee:
    def __init__(self, name):
        self.id = hash(name)
        self.name = name

    def __repr__(self):
        return self.name

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
        }
