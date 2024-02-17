
data = [
    {'nombre': 'certificado de bachiller', 'extension': 'pdf', 'tipo': 'certificado', 'tamaño': '1MB', 'nota': ''},
    {'nombre': 'acta de nacimiento', 'extension': 'pdf', 'tipo': 'documento oficial', 'tamaño': '500KB', 'nota': ''},
    {'nombre': 'carta de buena conducta', 'extension': 'pdf', 'tipo': 'carta', 'tamaño': '300KB', 'nota': ''},
    {'nombre': 'certificacion de estudios', 'extension': 'pdf', 'tipo': 'certificado', 'tamaño': '800KB', 'nota': ''},
]

def show_data():
    for item in data:
            print(f"Nombre: {item['nombre']}")

def search_function(query):

    #búsqueda en una lista de elementos

    results = [item for item in data if query.lower() in item['nombre'].lower()]
    return results

def update_document(nombre_documento, nueva_nota):
    for documento in data:
        if documento['nombre'] == nombre_documento:
            documento['nota'] = nueva_nota
            return "Documento actualizado"
    return "Documento no encontrado"