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
    def __init__(self, name, instrument, band_role):
        self.name = name
        self.instrument = instrument
        self.band_role = band_role
    pass

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"{self.band_role} instance. Name = {self.name}"

    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        pass


class Guitarist(Musician):
    def __init__(self, name):
        super().__init__(name, "guitar", Guitarist.__name__)


class Bassist(Musician):
    def __init__(self, name):
        super().__init__(name, "bass", Bassist.__name__)


class Drummer(Musician):
    def __init__(self, name):
        super().__init__(name, "drums", Drummer.__name__)


if __name__ == "__main__":
    pass
