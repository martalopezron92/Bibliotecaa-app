def libros(titulo, autor, anio):
    """Crea un diccionario que representa un libro con su título, autor y año de publicación.

    Args:
        titulo (str): El título del libro.
        autor (str): El autor del libro.
        anio (int): El año de publicación del libro.

    Returns:
        dict: Un diccionario con las claves 'titulo', 'autor' y 'anio'.
    """
    return {
        'titulo': titulo,
        'autor': autor,
        'anio': anio
    }