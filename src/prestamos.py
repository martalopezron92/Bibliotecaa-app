def prestamos(libro, usuario, fecha_prestamo):
    """Crea un diccionario que representa un préstamo de libro con el libro, usuario y fecha de préstamo.

    Args:
        libro (dict): Un diccionario que representa el libro prestado.
        usuario (str): El nombre del usuario que realiza el préstamo.
        fecha_prestamo (str): La fecha en que se realizó el préstamo.

    Returns:
        dict: Un diccionario con las claves 'libro', 'usuario' y 'fecha_prestamo'.
    """
    return {
        'libro': libro,
        'usuario': usuario,
        'fecha_prestamo': fecha_prestamo
    }