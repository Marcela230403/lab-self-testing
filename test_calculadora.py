# test_calculadora.py
import unittest
from calculadora import somar, subtrair
	
class TestCalculadora(unittest.TestCase):
    
    def test_somar(self):
        # Testa se 2 + 3 é igual a 5
        self.assertEqual(somar(2, 3), 5)
        
    def test_subtrair(self):
        # Testa se 10 - 4 é igual a 6
        self.assertEqual(subtrair(10, 4), 6)

if __name__ == '__main__':
    unittest.main() 