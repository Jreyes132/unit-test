def search(query):

    #búsqueda en una lista de elementos
    data = ['apple', 'banana', 'orange', 'grape']
    results = [item for item in data if query in item]

    return results
