class Band:
    pass

class Musician:
    def __init__(self, name="unknown"):
        self.name = name
    pass

class Guitarist(Musician):
    instrument = "guitar"
    solo = "face melting guitar solo"
    pass

class Bassist(Musician):
    pass

class Drummer(Musician):
    pass
