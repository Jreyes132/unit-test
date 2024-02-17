
data = [
      'certificado de bachiller', 
      'acta de nacimiento', 
      'carta de buena conducta', 
      'certificacion de estudios']

def show_data():
    for item in data:
            print(item)

def search_function(query):

    #búsqueda en una lista de elementos
    data = ['certificado de bachiller', 'acta de nacimiento', 'carta de buena conducta', 'certificacion de estudios']

    results = [item for item in data if query in item]
    return results
