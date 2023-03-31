class Band:
    pass

class Musician:
    def __init__(self, name="unknown"):
        self.name = name
    pass

class Guitarist(Musician):
    instrument = "guitar"
    pass

class Bassist(Musician):
    pass

class Drummer(Musician):
    pass