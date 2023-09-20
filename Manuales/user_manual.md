
### Manual de Usuario

---

#### Introducción

La "Aplicación Numérica con Análisis Léxico" es una herramienta que permite cargar, editar y analizar código fuente en formato JSON para identificar operaciones matemáticas y trigonométricas. Una vez analizado, el programa puede mostrar errores léxicos y proporcionar una representación gráfica de las operaciones en forma de árbol.

#### Inicio de la Aplicación

Al abrir la aplicación, se le presentará una interfaz gráfica con un menú en la parte superior y un área de texto en el centro.

#### Menú

1. **Archivo**:
   - **Abrir**: Le permite abrir un archivo existente para editarlo dentro de la aplicación.
   - **Guardar**: Guarda los cambios realizados en el archivo actualmente abierto.
   - **Guardar como**: Guarda el archivo con un nuevo nombre.
   - **Salir**: Cierra la aplicación.

2. **Analizar**: 
   - Al seleccionar esta opción, la aplicación analizará el código presente en el área de texto. Si hay errores, se mostrarán en un archivo JSON. Si no hay errores, se generará una representación gráfica de las operaciones.

3. **Errores**: 
   - Muestra los errores léxicos identificados durante el último análisis. Los errores se presentarán en un archivo con el formato `RESULTADOS_#202100106.json`.

4. **Reporte**: 
   - Genera y muestra diagramas de las operaciones identificadas utilizando la librería Graphviz.

#### Uso

1. Cargue un archivo JSON haciendo clic en `Archivo > Abrir`.
2. Edite el código según sea necesario.
3. Seleccione `Analizar` para iniciar el análisis léxico.
4. Si se identifican errores, vaya a `Errores` para ver los detalles.
5. Para ver una representación gráfica de las operaciones, seleccione `Reporte`.

#### Estructura del Archivo de Entrada

El archivo de entrada debe estar en formato JSON y seguir una estructura específica. Debe contener operaciones y configuraciones. Las operaciones definen las acciones matemáticas/trigonométricas a realizar, mientras que las configuraciones determinan las propiedades visuales de la representación gráfica.

Ejemplo:

```json
{
    "operaciones": [
        {
            "operacion": "suma",
            "valor1": 4.5,
            "valor2": 5.32
        },
        ...
    ],
    "configuraciones": [
        {
            "texto": "Operaciones",
            "fondo": "azul",
            "fuente": "blanco",
            "forma": "circulo"
        }
    ]
}
```

#### Consideraciones

- Asegúrese de que el archivo de entrada siga la estructura correcta para evitar errores léxicos.
- Las operaciones y configuraciones admiten anidamientos, lo que permite operaciones complejas y configuraciones visuales personalizadas.
- En caso de encontrar errores en el análisis, la aplicación generará un archivo JSON con detalles de los errores, incluyendo la posición y el tipo de error.

---
