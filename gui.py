import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
from lexer import *
from Errores import *
from Expresiones import *

class ScrollText(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.text = tk.Text(
            self,
            bg="#f8f9fa",
            foreground="#343a40",
            insertbackground="#3b5bdb",
            selectbackground="purple",
            width=120,
            height=25,
            font=("Monaco", 12),
        )

        self.scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.text.yview)
        self.text.configure(yscrollcommand=self.scrollbar.set)

        self.numberLines = TextLineNumbers(self, width=40, bg="#dee2e6")
        self.numberLines.attach(self.text)

        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.numberLines.pack(side=tk.LEFT, fill=tk.Y, padx=(5, 0))
        self.text.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.text.bind("<Key>", self.onPressDelay)
        self.text.bind("<Button-1>", self.numberLines.redraw)
        self.scrollbar.bind("<Button-1>", self.onScrollPress)
        self.text.bind("<MouseWheel>", self.onPressDelay)

    def onScrollPress(self, *args):
        self.scrollbar.bind("<B1-Motion>", self.numberLines.redraw)

    def onScrollRelease(self, *args):
        self.scrollbar.unbind("<B1-Motion>", self.numberLines.redraw)

    def onPressDelay(self, *args):
        self.after(2, self.numberLines.redraw)

    def get(self, *args, **kwargs):
        return self.text.get(*args, **kwargs)

    def insert(self, *args, **kwargs):
        return self.text.insert(*args, **kwargs)

    def delete(self, *args, **kwargs):
        return self.text.delete(*args, **kwargs)

    def index(self, *args, **kwargs):
        return self.text.index(*args, **kwargs)

    def redraw(self):
        self.numberLines.redraw()


class TextLineNumbers(tk.Canvas):

    def __init__(self, *args, **kwargs):
        tk.Canvas.__init__(self, *args, **kwargs, highlightthickness=0)
        self.textwidget = None

    def attach(self, text_widget):
        self.textwidget = text_widget

    def redraw(self, *args):
        """redraw line numbers"""
        self.delete("all")

        i = self.textwidget.index("@0,0")
        while True:
            dline = self.textwidget.dlineinfo(i)
            if dline is None:
                break
            y = dline[1]
            linenum = str(i).split(".")[0]
            self.create_text(
                2,
                y,
                anchor="nw",
                text=linenum,
                fill="#868e96",
                font=("Monaco", 12, "bold"),
            )
            i = self.textwidget.index("%s+1line" % i)

class VentanaBienvenida(tk.Tk):
    def __init__(self, app_class):
        super().__init__()
        self.title("Analizador Lexico")
        self.geometry("600x300")
        self.config(bg="#f79028")
        
        self.label = tk.Label(self, text="Bienvenido al Analizador Lexico", font=("Monaco", 20))
        self.label.pack(pady=40)
        
        self.start_button = tk.Button(self, text="Iniciar", command=self.launch_app, font=("Monaco", 16))
        self.start_button.pack(pady=20)
        
        self.quit_button = tk.Button(self, text="Salir", command=self.quit, font=("Monaco", 16))
        self.quit_button.pack(pady=20)
        
        self.app_class = app_class

    def launch_app(self):
        self.destroy()
        self.app = self.app_class()
        self.app.mainloop()


class Ventana(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Proyecto 1")
        self.geometry("1000x700")
        self.scroll = ScrollText(self)
        self.scroll.pack(fill=tk.BOTH, expand=True)
        self.after(200, self.scroll.redraw())

        self.menu = Menu(self)
        self.config(menu=self.menu)
        self.filemenu = Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.filemenu)
        self.filemenu.add_command(label="New")
        self.filemenu.add_command(label="Open...", command=self.open_file)
        self.filemenu.add_command(label="Save file...", command=self.save_file)

        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.quit)
        self.menu.add_command(label="Analizar", command=self.analizar_texto)
        self.menu.add_command(label="Ver reporte", command=self.mostrar_reporte)
        self.menu.add_command(label="Ver errores", command=self.errores)

     
    def open_file(self):
        filepath = askopenfilename(
            filetypes=[("JSON Files", "*.json"), ("All Files", "*.*")]
        )
        if not filepath:
            return
        
        self.scroll.delete(1.0,tk.END)
        with open(filepath, "r") as input_file:
            text = input_file.read()
            self.scroll.insert(tk.END, text)
        self.title(f"Proyecto 1 - {filepath}")

    def save_file(self):
        filepath = asksaveasfilename(
            defaultextension="json",
            filetypes=[("JSON Files", "*.json"), ("All Files", "*.*")],
        )
        if not filepath:
            return
        with open(filepath, "w") as output_file:
            text = self.scroll.get(1.0, tk.END)
            output_file.write(text)
        self.title(f"Proyecto 1 - {filepath}")

    def mostrar_mensajes_con_scroll(self, mensajes):
        win = Toplevel()
        win.title("Mensajes de Depuración")

        scrollbar = Scrollbar(win)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_widget = Text(win, wrap=tk.WORD, yscrollcommand=scrollbar.set, height=15, width=70)

        # Procesar y colorear el texto según los delimitadores
        while mensajes:
            if "[RED]" in mensajes:
                before, mensajes = mensajes.split("[RED]", 1)
                colored_text, mensajes = mensajes.split("[/RED]", 1)
                color_tag = "red_color"
            elif "[GREEN]" in mensajes:
                before, mensajes = mensajes.split("[GREEN]", 1)
                colored_text, mensajes = mensajes.split("[/GREEN]", 1)
                color_tag = "green_color"
            else:
                text_widget.insert(tk.END, mensajes)
                mensajes = ""

            # Insertar el texto que no necesita coloreado
            text_widget.insert(tk.END, before)

            # Guardar el índice de inicio donde se insertará el texto coloreado
            start_idx = text_widget.index(tk.END)
            # Insertar el texto que necesita coloreado
            text_widget.insert(tk.END, colored_text)
            # Guardar el índice de final después de la inserción del texto coloreado
            end_idx = text_widget.index(tk.END)
            # Aplicar la etiqueta de color al rango de texto coloreado
            text_widget.tag_add(color_tag, start_idx, end_idx)

        text_widget.tag_config("red_color", foreground="red")
        text_widget.tag_config("green_color", foreground="green")

        text_widget.config(state=tk.DISABLED)  # Hacer el widget de solo lectura
        text_widget.pack()

        scrollbar.config(command=text_widget.yview)


    def analizar_texto(self):
        limpiar_errores()
        text = self.scroll.get(1.0, tk.END).strip() 
        if not text:
            messagebox.showwarning("Advertencia", "El cuadro de texto está vacío. Por favor ingrese datos para analizar.")
            return
        
        debug_msgs = iniciar_analisis(text)

        if len(errores_lexicos) == 0:
            messagebox.showinfo("Info", "Análisis realizado con éxito!")
            debug_messages.append(arbol.dot.source)
            
        else:
            cantidad_errores = len(errores_lexicos)
            messagebox.showerror("Error", f"Se encontraron {cantidad_errores} errores en el análisis. Revise el reporte de errores.")
        # Mostrar mensajes de depuración en una ventana emergente
        if debug_msgs:
            debug_str = '\n'.join(debug_msgs)
            self.mostrar_mensajes_con_scroll(debug_str)


    def errores(self):
        if not errores_lexicos:
            messagebox.showerror("Error", "No hay errores, el texto está libre de errores o no se ha cargado un archivo")
            return
        else:
            debug_messages.clear()
            #Generar el reporte de errores
            nombre_archivo = "RESULTADOS_202100106.json"
            generar_reporte_errores(nombre_archivo)
        
            # Leer el contenido del archivo JSON
            with open(nombre_archivo, "r") as f:
                contenido_json = f.read()
            
            # Mostrar el contenido en una nueva ventana emergente
            ventana_errores = tk.Toplevel(self)
            ventana_errores.title("Reporte de Errores")
            ventana_errores.geometry("600x400")
            
            texto_widget = tk.Text(ventana_errores, wrap=tk.WORD)
            texto_widget.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
            texto_widget.insert(tk.END, contenido_json)
            
            # Hacer que el widget Text no sea editable
            texto_widget.config(state=tk.DISABLED)
            
            scrollbar = tk.Scrollbar(ventana_errores, command=texto_widget.yview)
            texto_widget.configure(yscrollcommand=scrollbar.set)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            
            messagebox.showinfo("Info", "Se ha generado el reporte de errores")

    def mostrar_reporte(self):
        global arbol  # Obtener el árbol generado en el análisis
        if arbol and arbol.dot and arbol.dot.body:
            arbol.dot.view("REPORTE_202100106")
        else:
            messagebox.showerror("Error", "No hay reporte para mostrar. Por favor, realice un análisis primero.")

            
app = VentanaBienvenida(Ventana)
app.mainloop()
