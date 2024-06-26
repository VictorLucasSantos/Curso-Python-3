import  unittest
from calculadora import soma

class TestClaculadora(unittest.TestCase):
    def test_soma_5_e_10_deve_retornar_15(self):
        self.assertEqual(soma(5, 10), 15)
        
    def test_subtracao_10_e_5_deve_retornar_5(self):
        self.assertEqual(soma(10, -5), 5)
        
    def test_soma_varias_entradas(self):
        x_y_saidas = (
            (10, 10, 20),
            (5, 5, 10),
            (1.5, 1.5, 3.0),
            (-5, 5, 0),
            (100, 100, 200),
        )
        for x_y_saidas  in x_y_saidas:
            with self.subTest(x_y_saidas=x_y_saidas):
                x, y, saida = x_y_saidas
                self.assertEqual(soma(x, y), saida)
                
    def test_soma_x_nao_e_int_ou_float_deve_raizar_excecao(self):
        with self.assertRaises(AssertionError):
            soma('11', 0)
            
unittest.main(verbosity=2)        