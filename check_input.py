__author__ = 'Orka'

def check_input(value1, value2):
    try:
        value1 = int(value1)
    except:
        ValueError
    try:
        value2 = int(value2)
    except:
        ValueError
    if type(value1) != int:
        value1 = 0
    if type(value2) != int or value2 <= 0:
        value2 = float('inf')
    return value1, value2


