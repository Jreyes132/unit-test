import pytest
from my_library import search

# Test de la función de actualización de notas
@pytest.mark.parametrize("nombre_documento, nueva_nota", [("certificado de bachiller", "Nota actualizada 1"), ("acta de nacimiento", "Nota actualizada 2"), ("carta de buena conducta", "Nota actualizada 3"), ("no existe", "Nota actualizada 4")])
def test_update_document_nota(nombre_documento, nueva_nota):
    nombre_documento = 'certificado de bachiller'
    nueva_nota = 'Nota actualizada'
    resultado =  search.update_document(nombre_documento, nueva_nota)
    assert resultado == "Documento actualizado"
  
# Test de la función de actualización de notas con documento inexistentes
@pytest.mark.parametrize("nombre_documento, nueva_nota", [("certificado de bachiller", "Nota actualizada 1"), ("acta de nacimiento", "Nota actualizada 2"), ("carta de buena conducta", "Nota actualizada 3"), ("no existe", "Nota actualizada 4")])
def test_update_nonexistent_document_nota(nombre_documento, nueva_nota):
    nombre_documento = 'documento inexistente'
    nueva_nota = 'Esta nota no debería agregarse'
    resultado = search.update_document(nombre_documento, nueva_nota)
    assert resultado == "Documento no encontrado"