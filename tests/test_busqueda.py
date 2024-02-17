
from my_library import login
from my_library import search
import pytest

# Usando la parametrización de pytest
@pytest.mark.parametrize("username, password", [("mg12345", "df12@434c"), ("invalid_username", "invalid_password")])
def test_login(username, password):
    assert login.login_function(username, password)
    assert not login.login_function('invalid_username', 'invalid_password')

@pytest.mark.parametrize("query", [("carta"), ("acta"), ("certificado"),('consulta_inexistente')])
def test_search(query):
    print()
    print("========================================================================================================")
    print("Datos de la búsqueda:")
    search.show_data()
    results = search.search_function(query)
    print("========================================================================================================")
    print("Resultados de la búsqueda:")
    for result in results:
        print(result)
    assert results
    assert search.search_function("consulta_inexistente") == []
