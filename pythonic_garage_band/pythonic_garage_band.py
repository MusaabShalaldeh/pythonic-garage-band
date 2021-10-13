

class Band:
    """
    Band Class
    """
    def __init__(self,name,members=[]):
        self.name = name
        self.members = members
        self.__class__.instances.append(self)

    def play_solos(self):
        plays = []
        for i in self.members:
            plays.append(i.play_solo())
        return plays

    def to_list():
        return __class__.instances



class Musician:
    """
    Musician Class
    """
    def __init__(self,instrument='',solo=''):
        self.instrument = instrument
        self.solo = solo

    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        return self.solo


class Guitarist(Musician):
    """
    Guitarist Class
    """
    def __init__(self,name):
        self.name = name
        self.instrument = 'guitar'
        self.solo = "face melting guitar solo"

    def __str__(self):
        return f"My name is {self.name} and I play guitar"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"
    

class Drummer(Musician):
    """
    Drummer Class
    """
    def __init__(self,name):
        self.name = name
        self.instrument = 'drums'
        self.solo = "rattle boom crash"

    def __str__(self):
        return f"My name is {self.name} and I play drums"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

class Bassist(Musician):
    """
    Bassist Class
    """
    def __init__(self,name):
        self.name = name
        self.instrument = 'bass'
        self.solo = "bom bom buh bom" 

    def __str__(self):
        return f"My name is {self.name} and I play bass"

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"





if __name__ == "__main__":
    testBand = Band()
    print(testBand)
    testMusician = Musician()
    print(testMusician)