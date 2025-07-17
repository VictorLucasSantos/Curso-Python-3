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

try:
    import sys
    import os

    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
except:
    raise
import unittest
from unittest.mock import patch
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
        self.assertFalse(self.clsPessoa.dados_obtidos)

    def test_obter_todos_os_dados_sucesso_ok(self):
        with patch("requests.get") as fake_request:
            fake_request.return_value.ok = True

            self.assertEqual(self.clsPessoa.obter_todos_os_dados(), "CONECTADO")
            self.assertTrue(self.clsPessoa.dados_obtidos)

    def test_obter_todos_os_dados_falha_404(self):
        with patch("requests.get") as fake_request:
            fake_request.return_value.ok = False

            self.assertEqual(self.clsPessoa.obter_todos_os_dados(), "ERRO 404")
            self.assertFalse(self.clsPessoa.dados_obtidos)

    def test_obter_todos_os_dados_e_falha_sequencial(self):
        with patch("requests.get") as fake_request:
            fake_request.return_value.ok = True

            self.assertEqual(self.clsPessoa.obter_todos_os_dados(), "CONECTADO")
            self.assertTrue(self.clsPessoa.dados_obtidos)

            fake_request.return_value.ok = False

            self.assertEqual(self.clsPessoa.obter_todos_os_dados(), "ERRO 404")
            self.assertFalse(self.clsPessoa.dados_obtidos)


if __name__ == "__main__":
    unittest.main(verbosity=2)
