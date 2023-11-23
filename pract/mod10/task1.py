import re

def is_valid_password(password):
    """
    Ограничения на пароли:
        • пароль должен содержать только латинские символы, цифры и специальные символы ^$%@#&*!?
        • пароль должен состоять из не менее чем шести символов
        • пароль должен содержать по крайней мере два латинских символа в верхнем регистре
        • пароль должен содержать по крайней мере одну цифру
        • пароль должен содержать по крайней мере два различных специальных символа
        • пароль не должен содержать трех одинаковых символов подряд

    >>> is_valid_password("rtG3FG!Tr^e")
    True
    >>> is_valid_password("aA1!*!1Aa")
    True
    >>> is_valid_password("oF^a1D@y5e6")
    True
    >>> is_valid_password("enroi#$rkdeR#$092uWedchf34tguv394h")
    True

    >>> is_valid_password("пароль")
    False
    >>> is_valid_password("password")
    False
    >>> is_valid_password("qwerty")
    False
    >>> is_valid_password("lOngPa$$$W0Rd")
    False
    """
    regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@$%^&*?])(?!.*(.)\1\1).{6,}$"

    return bool(re.match(regex, password))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
