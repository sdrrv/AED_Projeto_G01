import ctypes


class Cheats:
    def categoria(self):
        table = (3*ctypes.py_object)()
        table[0] = 'Medicina'
        table[1] = 'Enfermagem'
        table[2] = 'Auxiliar'
        return table

    def faixas(self):
        table = (3*ctypes.py_object)()
        table[0] = 'Jovem'
        table[1] = 'Adulto'
        table[2] = 'Idoso'
        return table

