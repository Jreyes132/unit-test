import unittest
from My_library import login 
from My_library import search

class TestYourModule(unittest.TestCase):

    def test_login(self):
        # Caso de prueba exitoso
        assert login.login('valid_username', 'valid_password')

        # Caso de prueba fallido
        assert not login.login('invalid_username', 'invalid_password')

    def test_search(self):
        # Caso de prueba con resultados
        assert search.search('query_with_results'), ['apple', 'grape']

        # Caso de prueba sin resultados
        assert search.search('query_without_results'), []
