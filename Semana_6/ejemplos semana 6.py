def es_parentesis(caracter):
    """

    (str of len ==1) -> str

    >>> es_parentesis('(')
    'Es parentesis'

    >>> es_parentesis('x')
    'No es parentesis'

    >>> es_parentesis('xa')
    Traceback (most recent call last):
    ..
    TypeError: xa no es un parentesis

    :param caracter: str el caracter a evaluar
    :return: str el mensaje de la validacion
    """

    if len(caracter) != 1:
        raise TypeError(str(caracter) + ' no es un parentesis')
    elif caracter in '()': # caracter == '(' or caracter == ')':
        return 'Es parentesis'
    return 'No es parentesis'


