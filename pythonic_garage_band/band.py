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
    def __init__(self, name, instrument, band_role, solo):
        self.name = name
        self.instrument = instrument
        self.band_role = band_role
        self.solo = solo

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"{self.band_role} instance. Name = {self.name}"

    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        return self.solo


class Guitarist(Musician):
    def __init__(self, name):
        instrument = "guitar"
        solo = "face melting guitar solo"  # coulda shoulda been "wah-wah, wah-wah"
        super().__init__(name, instrument, Guitarist.__name__, solo)


class Bassist(Musician):
    def __init__(self, name):
        instrument = "bass"
        solo = "bom bom buh bom"
        super().__init__(name, instrument, Bassist.__name__, solo)


class Drummer(Musician):
    def __init__(self, name):
        instrument = "drums"
        solo = "rattle boom crash"
        super().__init__(name, instrument, Drummer.__name__, solo)


if __name__ == "__main__":
    pass
