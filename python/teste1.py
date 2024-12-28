import unittest
from psomar import somar

# Função a ser testada

# Classe de teste
class TestSoma(unittest.TestCase):

    def test_soma(self):
        # Testando se a soma de 3 e 2 é 5
        self.assertEqual(somar(3, 2), 5)

    def test_soma_negativos(self):
        # Testando soma com números negativos
        self.assertEqual(somar(-1, -1), -2)

    def test_soma_zero(self):
        # Testando soma com zero
        self.assertEqual(somar(0, 5), 5)

# Rodando os testes
if __name__ == '__main__':
    unittest.main()
