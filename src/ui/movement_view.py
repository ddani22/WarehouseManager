# Vista gráfica de movimientos
import tkinter as tk
from tkinter import ttk, messagebox
from src.core.inventory_manager import InventoryManager

class MovementView(ttk.Frame):
    """
    Pestaña gráfica para gestionar movimientos en el almacén.
    """
    def __init__(self, master=None):
        super().__init__(master)
        # Instancia el gestor de inventario para acceder a la lógica de negocio
        self.manager = InventoryManager()
        self._crear_widgets()
        self._cargar_movimientos()

    def _crear_widgets(self):
        """
        Crea los widgets de la interfaz: barra de búsqueda, tabla de movimientos y botones de acción.
        """
        # Frame para barra de búsqueda
        self.frame_busqueda = ttk.Frame(self)
        self.frame_busqueda.pack(fill=tk.X, padx=10, pady=(10,0))
        ttk.Label(self.frame_busqueda, text="Buscar por fecha de movimiento:").pack(side=tk.LEFT)
        self.entry_busqueda = ttk.Entry(self.frame_busqueda)
        self.entry_busqueda.pack(side=tk.LEFT, padx=5)
        btn_buscar = ttk.Button(self.frame_busqueda, text="Buscar", command=self._filtrar_movimientos)
        btn_buscar.pack(side=tk.LEFT)
        btn_limpiar = ttk.Button(self.frame_busqueda, text="Limpiar", command=self._limpiar_busqueda)
        btn_limpiar.pack(side=tk.LEFT, padx=5)

        self.frame_lista = ttk.Frame(self)
        self.frame_lista.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Tabla para mostrar los movimientos
        self.tree = ttk.Treeview(self.frame_lista, columns=("ID", "Producto", "Tipo", "Cantidad", "Fecha", "Referencia", "Usuario", "Cliente/Proveedor"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Botones para registrar y eliminar movimientos
        self.frame_botones = ttk.Frame(self)
        self.frame_botones.pack(pady=10)

        self.btn_agregar = ttk.Button(self.frame_botones, text="Registrar movimiento", command=self._abrir_agregar)
        self.btn_agregar.grid(row=0, column=0, padx=5)
        self.btn_eliminar = ttk.Button(self.frame_botones, text="Eliminar movimiento", command=self._eliminar_movimiento)
        self.btn_eliminar.grid(row=0, column=1, padx=5)

    def _cargar_movimientos(self, movimientos=None):
        """
        Carga la lista de movimientos en la tabla. Si se pasa una lista, la usa; si no, carga todos.
        """
        for item in self.tree.get_children():
            self.tree.delete(item)
        if movimientos is None:
            movimientos = self.manager.listar_movimientos()
        for m in movimientos:
            self.tree.insert("", tk.END, values=(m.id_movimiento, m.id_producto, m.tipo_movimiento, m.cantidad, m.fecha_movimiento, m.referencia_origen, m.id_usuario, m.id_cliente_proveedor))

    def _filtrar_movimientos(self):
        """
        Filtra los movimientos por fecha según el texto de búsqueda.
        """
        texto = self.entry_busqueda.get().lower()
        todos = self.manager.listar_movimientos()
        filtrados = [m for m in todos if texto in str(m.fecha_movimiento).lower()]
        self._cargar_movimientos(filtrados)

    def _limpiar_busqueda(self):
        """
        Limpia la barra de búsqueda y muestra todos los movimientos.
        """
        self.entry_busqueda.delete(0, tk.END)
        self._cargar_movimientos()

    def _abrir_agregar(self):
        """
        Abre una ventana para registrar un nuevo movimiento, con validaciones básicas de tipo de dato.
        """
        win = tk.Toplevel(self)
        win.title("Registrar movimiento")
        win.geometry("400x400")
        labels = ["ID", "Producto", "Tipo (entrada/salida)", "Cantidad", "Fecha", "Referencia", "Usuario", "Cliente/Proveedor"]
        entries = []
        for i, label in enumerate(labels):
            ttk.Label(win, text=label).grid(row=i, column=0, pady=5, sticky=tk.W)
            entry = ttk.Entry(win)
            entry.grid(row=i, column=1, pady=5)
            entries.append(entry)

        def guardar():
            """
            Valida los datos ingresados y registra el movimiento si son correctos.
            """
            try:
                datos = [e.get() for e in entries]
                # Validación de ID (debe ser entero y único)
                if not datos[0].isdigit():
                    messagebox.showerror("Error", "El ID debe ser un número entero.")
                    return
                movimientos_existentes = self.manager.listar_movimientos()
                if any(m.id_movimiento == int(datos[0]) for m in movimientos_existentes):
                    messagebox.showerror("Error", f"El ID {datos[0]} ya existe para otro movimiento.")
                    return
                datos[0] = int(datos[0])
                datos[1] = int(datos[1])
                datos[3] = int(datos[3])
                datos[6] = int(datos[6])
                datos[7] = int(datos[7])
                self.manager.registrar_movimiento(*datos)
                messagebox.showinfo("Éxito", "Movimiento registrado correctamente")
                win.destroy()
                self._cargar_movimientos()
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo registrar el movimiento: {e}")

        btn_guardar = ttk.Button(win, text="Guardar", command=guardar)
        btn_guardar.grid(row=len(labels), column=0, columnspan=2, pady=10)

    def _eliminar_movimiento(self):
        """
        Elimina el movimiento seleccionado de la tabla y la base de datos.
        """
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showwarning("Advertencia", "Seleccione un movimiento para eliminar")
            return
        id_movimiento = self.tree.item(seleccionado[0])["values"][0]
        self.manager.eliminar_movimiento(id_movimiento)
        self._cargar_movimientos()
        messagebox.showinfo("Éxito", "Movimiento eliminado")
