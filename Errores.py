import json

class ErrorLexico:
    def __init__(self, lexema, tipo, columna, fila):
        self.lexema = lexema
        self.tipo = tipo
        self.columna = columna
        self.fila = fila

errores_lexicos = []

def agregar_error(lexema, tipo, columna, fila):
    error = ErrorLexico(lexema, tipo, columna, fila)
    errores_lexicos.append(error)

def generar_reporte_errores(nombre_archivo="RESULTADOS_202100106.json"):
    data = {"errores": [{"No.": i+1, "descripcion": vars(error)} for i, error in enumerate(errores_lexicos)]}
    with open(nombre_archivo, "w") as f:
        json.dump(data, f, indent=4)
        

def limpiar_errores():
    errores_lexicos.clear()
