# Vista gráfica de productos
import tkinter as tk
from tkinter import ttk, messagebox
from src.core.inventory_manager import InventoryManager

class ProductView(ttk.Frame):
    """
    Pestaña gráfica para gestionar productos en el almacén.
    """
    def __init__(self, master=None):
        super().__init__(master)
        # Instancia el gestor de inventario para acceder a la lógica de negocio
        self.manager = InventoryManager()
        self._crear_widgets()
        self._cargar_productos()

    def _crear_widgets(self):
        """
        Crea los widgets de la interfaz: barra de búsqueda, tabla de productos y botones de acción.
        """
        # Frame para barra de búsqueda
        self.frame_busqueda = ttk.Frame(self)
        self.frame_busqueda.pack(fill=tk.X, padx=10, pady=(10,0))
        ttk.Label(self.frame_busqueda, text="Buscar por nombre de producto:").pack(side=tk.LEFT)
        self.entry_busqueda = ttk.Entry(self.frame_busqueda)
        self.entry_busqueda.pack(side=tk.LEFT, padx=5)
        btn_buscar = ttk.Button(self.frame_busqueda, text="Buscar", command=self._filtrar_productos)
        btn_buscar.pack(side=tk.LEFT)
        btn_limpiar = ttk.Button(self.frame_busqueda, text="Limpiar", command=self._limpiar_busqueda)
        btn_limpiar.pack(side=tk.LEFT, padx=5)

        self.frame_lista = ttk.Frame(self)
        self.frame_lista.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Tabla para mostrar los productos
        self.tree = ttk.Treeview(self.frame_lista, columns=("ID", "Nombre", "Descripción", "SKU", "Precio", "Stock", "Mínimo", "Ubicación", "Proveedor", "Fecha"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=80)
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Botones para agregar y eliminar productos
        self.frame_botones = ttk.Frame(self)
        self.frame_botones.pack(pady=10)

        self.btn_agregar = ttk.Button(self.frame_botones, text="Agregar producto", command=self._abrir_agregar)
        self.btn_agregar.grid(row=0, column=0, padx=5)
        self.btn_eliminar = ttk.Button(self.frame_botones, text="Eliminar producto", command=self._eliminar_producto)
        self.btn_eliminar.grid(row=0, column=1, padx=5)

    def _cargar_productos(self, productos=None):
        """
        Carga la lista de productos en la tabla. Si se pasa una lista, la usa; si no, carga todos.
        """
        for item in self.tree.get_children():
            self.tree.delete(item)
        if productos is None:
            productos = self.manager.listar_productos()
        for p in productos:
            self.tree.insert("", tk.END, values=(p.id_producto, p.nombre_producto, p.descripcion, p.sku, p.precio_unitario, p.stock_actual, p.stock_minimo, p.ubicacion, p.id_proveedor, p.fecha_alta))

    def _filtrar_productos(self):
        """
        Filtra los productos por nombre según el texto de búsqueda.
        """
        texto = self.entry_busqueda.get().lower()
        todos = self.manager.listar_productos()
        filtrados = [p for p in todos if texto in p.nombre_producto.lower()]
        self._cargar_productos(filtrados)

    def _limpiar_busqueda(self):
        """
        Limpia la barra de búsqueda y muestra todos los productos.
        """
        self.entry_busqueda.delete(0, tk.END)
        self._cargar_productos()

    def _abrir_agregar(self):
        """
        Abre una ventana para agregar un nuevo producto, con validaciones de campos numéricos.
        """
        win = tk.Toplevel(self)
        win.title("Agregar producto")
        win.geometry("400x400")
        labels = ["ID", "Nombre", "Descripción", "SKU", "Precio unitario", "Stock actual", "Stock mínimo", "Ubicación", "ID proveedor", "Fecha alta (YYYY-MM-DD)"]
        entries = []
        for i, label in enumerate(labels):
            ttk.Label(win, text=label).grid(row=i, column=0, pady=5, sticky=tk.W)
            entry = ttk.Entry(win)
            entry.grid(row=i, column=1, pady=5)
            entries.append(entry)

        def es_entero(valor):
            """
            Valida si el valor es un entero positivo.
            """
            return valor.isdigit()

        def es_flotante(valor):
            """
            Valida si el valor es un número flotante positivo.
            """
            try:
                return float(valor) >= 0
            except ValueError:
                return False

        def guardar():
            """
            Valida los datos ingresados y agrega el producto si son correctos.
            """
            try:
                datos = [e.get() for e in entries]
                # Validaciones de campos numéricos
                if not es_entero(datos[0]):
                    messagebox.showerror("Error", "El ID debe ser un número entero.")
                    return
                # Validación de ID único
                productos_existentes = self.manager.listar_productos()
                if any(p.id_producto == int(datos[0]) for p in productos_existentes):
                    messagebox.showerror("Error", f"El ID {datos[0]} ya existe para otro producto.")
                    return
                if not es_flotante(datos[4]):
                    messagebox.showerror("Error", "El precio unitario debe ser un número positivo.")
                    return
                if not es_entero(datos[5]):
                    messagebox.showerror("Error", "El stock actual debe ser un número entero.")
                    return
                if not es_entero(datos[6]):
                    messagebox.showerror("Error", "El stock mínimo debe ser un número entero.")
                    return
                if not es_entero(datos[8]):
                    messagebox.showerror("Error", "El ID proveedor debe ser un número entero.")
                    return
                # Conversión de tipos
                datos[0] = int(datos[0])
                datos[4] = float(datos[4])
                datos[5] = int(datos[5])
                datos[6] = int(datos[6])
                datos[8] = int(datos[8])
                self.manager.agregar_producto(*datos)
                messagebox.showinfo("Éxito", "Producto agregado correctamente")
                win.destroy()
                self._cargar_productos()
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo agregar el producto: {e}")

        btn_guardar = ttk.Button(win, text="Guardar", command=guardar)
        btn_guardar.grid(row=len(labels), column=0, columnspan=2, pady=10)

    def _eliminar_producto(self):
        """
        Elimina el producto seleccionado de la tabla y la base de datos.
        """
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showwarning("Advertencia", "Seleccione un producto para eliminar")
            return
        id_producto = self.tree.item(seleccionado[0])["values"][0]
        self.manager.eliminar_producto(id_producto)
        self._cargar_productos()
        messagebox.showinfo("Éxito", "Producto eliminado")
