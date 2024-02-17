# importando modulos
from my_library import login
from my_library import search
import pytest

# Test de la función de inicio de sesión
@pytest.mark.parametrize("username, password", [("mg12345", "df12@434c"), ("invalid_username", "invalid_password")])
def test_login(username, password):
    """
    Prueba la función de inicio de sesión con credenciales válidas e inválidas.
    """
    assert login.login_function(username, password)
    assert not login.login_function('invalid_username', 'invalid_password')

# Test de la función de búsqueda
@pytest.mark.parametrize("query", [("carta"), ("acta"), ("certificado"),('consulta_inexistente')])
def test_search(query):
    """
    Prueba la función de búsqueda con diferentes consultas.
    """
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
