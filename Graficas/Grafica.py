import graphviz
import time

class Arbolito:
    # Diccionario de traducciones
    traducciones = {
        "rojo": "red",
        "azul": "blue",
        "verde": "green",
        "amarillo": "yellow",
        "naranja": "orange",
        "morado": "purple",
        "negro": "black",
        "blanco": "white",
        "gris": "gray",
        "rosa": "pink",
        "cian": "cyan",
        "magenta": "magenta",
        "café": "brown",
        "cafe": "brown",
        "transparente": "transparent",
        "círculo": "circle",
        "circulo": "circle",
        "cuadrado": "square",
        "rectángulo": "rectangle",
        "rectangulo": "rectangle",
        "rombo": "diamond",
        "triángulo": "triangle",
        "triangulo": "triangle",
        "pentágono": "pentagon",
        "pentagono": "pentagon",
        "hexágono": "hexagon",
        "hexagono": "hexagon",
        "octágono": "octagon",
        "octagono": "octagon",
        "elipse": "ellipse",
        "ovalo": "oval",
        "punto": "point",
        "huevo": "egg",
        "trapecio": "trapezium",
        "paralelogramo": "parallelogram",

    }


    def __init__(self):
        timestr = time.strftime("%Y%m%d-%H%M%S")
        self.dot = graphviz.Digraph(comment=f"Graph {timestr}")
        self.counter = 0

    def agregarConfiguracion(self, confg):
        # Traducir los valores al inglés
        fondo = Arbolito.traducciones.get(confg["fondo"], confg["fondo"])
        fuente = Arbolito.traducciones.get(confg["fuente"], confg["fuente"])
        forma = Arbolito.traducciones.get(confg["forma"], confg["forma"])

        self.dot.attr(
            "node",
            style="filled",
            fillcolor=fondo,
            fontcolor=fuente,
            shape=forma,
        )

    def agregarNodo(self, valor):
        nombre = f"nodo{self.counter}"
        self.dot.node(nombre, valor)
        self.counter += 1
        return nombre

    def agregarArista(self, nodo1: str, nodo2: str):
        self.dot.edge(nodo1, nodo2)

    def generarGrafica(self):
        self.dot.render("Graficas/Arbol", view=True)
        self.dot.save("Graficas/Arbol.dot")

    def obtenerUltimoNodo(self):
        return f"nodo{self.counter - 1}"

arbol = Arbolito()
