"""
class Pessoa
    __init__
        nome str
        sobrenome str
        dados_obtidos bool (inicia False)

    API:
        obter_todos_os_dados -> method
            OK
            404

            (dados_obtidos se torna True se dados obtidos com sucesso)
"""

import unittest
from pessoa import Pessoa


class TesPessoa(unittest.TestCase):
    def setUp(self):
        self.clsPessoa = Pessoa("Victor", "Lucas")

    def test_pessoa_attr_nome_tem_valor_correto(self):
        self.assertEqual(self.clsPessoa.nome, "Victor")

    def test_pessoa_attr_nome_e_str(self):
        self.assertIsInstance(self.clsPessoa.nome, str)

    def test_pessoa_attr_sobrenome_tem_valor_correto(self):
        self.assertEqual(self.clsPessoa.sobrenome, "Lucas")

    def test_pessoa_attr_sobrenome_e_str(self):
        self.assertIsInstance(self.clsPessoa.sobrenome, str)

    def test_pessoa_attr_dados_obtidos_inicia_false(self):
        self.assertFalse(self.clsPessoa.dados_obtidos, False)


if __name__ == "__main__":
    unittest.main(verbosity=2)
