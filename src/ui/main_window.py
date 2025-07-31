"""
Ventana principal de la aplicación con pestañas.
Este archivo define la interfaz principal y la estructura de navegación entre las vistas de productos, clientes, proveedores y movimientos.
"""
import tkinter as tk
from tkinter import ttk
from src.ui.product_view import ProductView
from src.ui.client_view import ClientView  # Asegúrate de que src/ui/client_view.py existe y define ClientView
from src.ui.supplier_view import SupplierView
from src.ui.movement_view import MovementView

class PlaceholderView(ttk.Frame):
    """
    Vista de marcador de posición para futuras pestañas o mensajes.
    """
    def __init__(self, master, texto):
        super().__init__(master)
        label = ttk.Label(self, text=texto, font=("Arial", 12))
        label.pack(pady=20)

class MainWindow(tk.Tk):
    """
    Ventana principal gráfica con pestañas para gestionar productos, clientes, proveedores y movimientos.
    """
    def __init__(self):
        super().__init__()
        # Configura el título y tamaño de la ventana principal
        self.title("Gestión de Almacén")
        self.geometry("900x500")
        self._crear_widgets()

    def _crear_widgets(self):
        """
        Crea el widget Notebook y agrega las pestañas de cada módulo principal.
        """
        notebook = ttk.Notebook(self)
        notebook.pack(fill=tk.BOTH, expand=True)

        # Pestaña de productos
        tab_productos = ProductView(master=notebook)
        notebook.add(tab_productos, text="Productos")

        # Pestaña de clientes
        tab_clientes = ClientView(master=notebook)
        notebook.add(tab_clientes, text="Clientes")

        # Pestaña de proveedores
        tab_proveedores = SupplierView(master=notebook)
        notebook.add(tab_proveedores, text="Proveedores")

        # Pestaña de movimientos
        tab_movimientos = MovementView(master=notebook)
        notebook.add(tab_movimientos, text="Movimientos")

# Punto de entrada de la aplicación
if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
