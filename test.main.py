from main import somar

def test_soma():
    resultado = somar(2, 3)
    assert resultado["resultado"] == 5