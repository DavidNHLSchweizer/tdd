class NaamError(Exception):
    pass

class Naam:
    def __init__(self, achternaam='', voornaam=''):
        if not achternaam:
            raise NaamError(f'Achternaam leeg (ingevoerd: {achternaam=}')
        self.achternaam = achternaam
        self.voornaam = voornaam