from Expresiones.expresion import *
import math
from Graficas.Grafica import *


class ExpresionTrigonometrica(Expresion):
    def __init__(self, tipo, valor, linea, columna):
        self.tipo = tipo
        self.valor = valor
        self.linea = linea
        self.columna = columna

    def interpretar(self):
        valor = self.valor

        # nombre de las etiquetas
        nodo = None

        # validar si es un numero o una Expresion
        if isinstance(self.valor, Expresion):
            valor = self.valor.interpretar()
            nodo = arbol.obtenerUltimoNodo()
        else:
            valor = self.valor
            nodo = arbol.agregarNodo(str(valor))

        print("`" * 20)
        print("tipo: ", self.tipo)
        print("valor: ", valor)
        resultado = None
        if self.tipo == "seno":
            resultado = math.sin(valor)
        elif self.tipo == "coseno":
            resultado = math.cos(valor)
        elif self.tipo == "tangente":
            resultado = math.tan(valor)
        elif self.tipo == "inverso":
            if valor == 0:
                return "Error: inverso entre 0"
            resultado = 1 / valor
        else:
            return "Error: tipo de operacion no valida"
            

        # GRAFICAR
        raiz = arbol.agregarNodo(self.tipo + "\\n" + "{:.4f}".format(resultado))
        arbol.agregarArista(raiz, nodo)

        return round(resultado, 2)
