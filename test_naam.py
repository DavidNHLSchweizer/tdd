from naam import Naam

def test_init_empty():
    n = Naam()
    assert n.voornaam == ''
    assert n.achternaam == ''

def test_init_achternaam():
    n = Naam('Dijkstra')
    assert n.voornaam == ''
    assert n.achternaam == 'Dijkstra'

def test_init_achternaam():
    n = Naam('Dijkstra', 'Tsjibbe')
    assert n.voornaam == 'Tsjibbe'
    assert n.achternaam == 'Dijkstra'
    
def test_change_achternaam():
    n = Naam('Dijkstra', 'Tsjibbe')
    n.achternaam = 'Dijkema'
    assert n.voornaam == 'Tsjibbe'
    assert n.achternaam == 'Dijkema'

def test_change_naam():
    n = Naam('Dijkstra', 'Tsjibbe')
    n.achternaam = 'Dijkema'
    n.voornaam = 'Sjoukje'
    assert n.voornaam == 'Sjoukje'
    assert n.achternaam == 'Dijkema'
