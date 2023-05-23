class Band:
    def __init__(self, name="unknown", members=[]):
        self.name = name
        self.members = members

    def play_solos(self):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def to_list(self):
        pass


class Musician:
    def __init__(self, name="", instrument=""):
        self.name = name
        self.instrument = instrument
    pass

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        pass

    def get_instrument(self):
        pass

    def play_solo(self):
        pass


class Guitarist(Musician):
    def __init__(self, name):
        super().__init__(name, "guitar")


class Bassist(Musician):
    pass


class Drummer(Musician):
    pass


if __name__ == "__main__":
    pass
