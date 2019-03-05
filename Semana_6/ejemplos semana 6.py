def es_parentesis(caracter):
    """

    (str of len ==1) -> str

    >>> es_parentesis('(')
    'Es parentesis'

    >>> es_parentesis('x')
    'No Es parentesis'

    >>> es_parentesis('xa')
    Tracebackv (most recent call last):
    ..
    TypeError: xa no es un parentesis

    :param caracter: str el caracter a evaluar
    :return: str el mensaje de la validacion
    """

