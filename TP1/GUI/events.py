"""
    events.py

    Diccionario de eventos apuntando a su respectiva función
"""


def ws_test():
    """
        retorna un "OK", esta definición de evento es redundante, es solo para ilustrar
    """
    return "OK"


events = {
    "ws-test": ws_test,
}


