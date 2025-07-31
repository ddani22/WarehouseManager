# Vista gráfica de proveedores
import tkinter as tk
from tkinter import ttk, messagebox
from src.core.inventory_manager import InventoryManager

class SupplierView(ttk.Frame):
    """
    Pestaña gráfica para gestionar proveedores en el almacén.
    """
    def __init__(self, master=None):
        super().__init__(master)
        # Instancia el gestor de inventario para acceder a la lógica de negocio
        self.manager = InventoryManager()
        self._crear_widgets()
        self._cargar_proveedores()

    def _crear_widgets(self):
        """
        Crea los widgets de la interfaz: barra de búsqueda, tabla de proveedores y botones de acción.
        """
        # Frame para barra de búsqueda
        self.frame_busqueda = ttk.Frame(self)
        self.frame_busqueda.pack(fill=tk.X, padx=10, pady=(10,0))
        ttk.Label(self.frame_busqueda, text="Buscar por nombre de proveedor:").pack(side=tk.LEFT)
        self.entry_busqueda = ttk.Entry(self.frame_busqueda)
        self.entry_busqueda.pack(side=tk.LEFT, padx=5)
        btn_buscar = ttk.Button(self.frame_busqueda, text="Buscar", command=self._filtrar_proveedores)
        btn_buscar.pack(side=tk.LEFT)
        btn_limpiar = ttk.Button(self.frame_busqueda, text="Limpiar", command=self._limpiar_busqueda)
        btn_limpiar.pack(side=tk.LEFT, padx=5)

        self.frame_lista = ttk.Frame(self)
        self.frame_lista.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Tabla para mostrar los proveedores
        self.tree = ttk.Treeview(self.frame_lista, columns=("ID", "Nombre", "Teléfono", "Email", "Dirección"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120)
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Botones para agregar y eliminar proveedores
        self.frame_botones = ttk.Frame(self)
        self.frame_botones.pack(pady=10)

        self.btn_agregar = ttk.Button(self.frame_botones, text="Agregar proveedor", command=self._abrir_agregar)
        self.btn_agregar.grid(row=0, column=0, padx=5)
        self.btn_eliminar = ttk.Button(self.frame_botones, text="Eliminar proveedor", command=self._eliminar_proveedor)
        self.btn_eliminar.grid(row=0, column=1, padx=5)

    def _cargar_proveedores(self, proveedores=None):
        """
        Carga la lista de proveedores en la tabla. Si se pasa una lista, la usa; si no, carga todos.
        """
        for item in self.tree.get_children():
            self.tree.delete(item)
        if proveedores is None:
            proveedores = self.manager.listar_proveedores()
        for p in proveedores:
            self.tree.insert("", tk.END, values=(p.id_proveedor, p.nombre_proveedor, p.telefono, p.email, p.direccion))

    def _filtrar_proveedores(self):
        """
        Filtra los proveedores por nombre según el texto de búsqueda.
        """
        texto = self.entry_busqueda.get().lower()
        todos = self.manager.listar_proveedores()
        filtrados = [p for p in todos if texto in p.nombre_proveedor.lower()]
        self._cargar_proveedores(filtrados)

    def _limpiar_busqueda(self):
        """
        Limpia la barra de búsqueda y muestra todos los proveedores.
        """
        self.entry_busqueda.delete(0, tk.END)
        self._cargar_proveedores()

    def _abrir_agregar(self):
        """
        Abre una ventana para agregar un nuevo proveedor, con validaciones de email y teléfono.
        """
        win = tk.Toplevel(self)
        win.title("Agregar proveedor")
        win.geometry("350x300")
        labels = ["ID", "Nombre", "Teléfono", "Email", "Dirección"]
        entries = []
        for i, label in enumerate(labels):
            ttk.Label(win, text=label).grid(row=i, column=0, pady=5, sticky=tk.W)
            entry = ttk.Entry(win)
            entry.grid(row=i, column=1, pady=5)
            entries.append(entry)

        def validar_email(email):
            """
            Verifica si el email tiene un formato válido.
            """
            import re
            patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
            return re.match(patron, email)

        def validar_telefono(telefono):
            """
            Verifica si el teléfono tiene un formato válido (solo dígitos, mínimo 7).
            """
            return telefono.isdigit() and 7 <= len(telefono) <= 15

        def guardar():
            """
            Valida los datos ingresados y agrega el proveedor si son correctos.
            """
            try:
                datos = [e.get() for e in entries]
                # Validación de ID (debe ser entero y único)
                if not datos[0].isdigit():
                    messagebox.showerror("Error", "El ID debe ser un número entero.")
                    return
                proveedores_existentes = self.manager.listar_proveedores()
                if any(p.id_proveedor == int(datos[0]) for p in proveedores_existentes):
                    messagebox.showerror("Error", f"El ID {datos[0]} ya existe para otro proveedor.")
                    return
                datos[0] = int(datos[0])
                # Validación de teléfono
                if not validar_telefono(datos[2]):
                    messagebox.showerror("Error", "El número de teléfono no es válido. Debe contener solo dígitos y tener entre 7 y 15 caracteres.")
                    return
                # Validación de email
                if not validar_email(datos[3]):
                    messagebox.showerror("Error", "El email no tiene un formato válido.")
                    return
                self.manager.agregar_proveedor(*datos)
                messagebox.showinfo("Éxito", "Proveedor agregado correctamente")
                win.destroy()
                self._cargar_proveedores()
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo agregar el proveedor: {e}")

        btn_guardar = ttk.Button(win, text="Guardar", command=guardar)
        btn_guardar.grid(row=len(labels), column=0, columnspan=2, pady=10)

    def _eliminar_proveedor(self):
        """
        Elimina el proveedor seleccionado de la tabla y la base de datos.
        """
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showwarning("Advertencia", "Seleccione un proveedor para eliminar")
            return
        id_proveedor = self.tree.item(seleccionado[0])["values"][0]
        self.manager.eliminar_proveedor(id_proveedor)
        self._cargar_proveedores()
        messagebox.showinfo("Éxito", "Proveedor eliminado")
