
### Manual Técnico

---

#### Introducción

La aplicación "Aplicación Numérica con Análisis Léxico" es una herramienta desarrollada en Python que permite el análisis léxico de un código fuente en formato JSON. Esta herramienta reconoce un conjunto específico de operaciones matemáticas y trigonométricas, y proporciona una representación visual de las operaciones en forma de un árbol utilizando la biblioteca Graphviz.

#### Estructura del Programa

El programa se compone de los siguientes archivos:

1. **main.py**: Punto de entrada de la aplicación.
2. **gui.py**: Gestiona la interfaz gráfica del usuario (GUI) utilizando la biblioteca `tkinter`.
3. **lexer.py**: Realiza el análisis léxico del código fuente.
4. **Arbol.py**: Funciones y clases relacionadas con la generación y representación de árboles.
5. **aritmeticas.py** y **trigonometricas.py**: Define operaciones aritméticas y trigonométricas respectivamente.

#### Descripción Detallada

- **main.py**: 
  - Inicializa y lanza la interfaz gráfica.
  
- **gui.py**: 
  - Define la interfaz gráfica, incluyendo menús, botones y áreas de texto.
  - Maneja eventos como abrir archivos, guardar, analizar el código, etc.
  
- **lexer.py**: 
  - Realiza el análisis léxico del código fuente, identificando tokens y estructurando el código.
  - Identifica errores léxicos y los registra para su posterior visualización.
  
- **Arbol.py**: 
  - Genera una representación visual en forma de árbol de las operaciones identificadas.
  - Utiliza la biblioteca `graphviz` para crear y visualizar el árbol.
  
- **aritmeticas.py** y **trigonometricas.py**:
  - Define las operaciones matemáticas y trigonométricas respectivamente.
  - Cada operación tiene una representación en forma de clase que puede evaluar la operación y devolver un resultado.
  
- **expresion.py**:
  - Define una clase abstracta `Expresion` que sirve como base para otras clases de expresiones.
  - Establece un contrato para que todas las expresiones implementen un método `interpretar`.

#### Dependencias

- `tkinter`: Para la interfaz gráfica.
- `graphviz`: Para la visualización de árboles.
- Otras bibliotecas estándar de Python como `collections`, `math`, etc.

---
