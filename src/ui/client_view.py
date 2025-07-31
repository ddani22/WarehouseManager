# Vista gráfica de clientes
import tkinter as tk
from tkinter import ttk, messagebox
from src.core.inventory_manager import InventoryManager

class ClientView(ttk.Frame):
    """
    Pestaña gráfica para gestionar clientes en el almacén.
    """
    def __init__(self, master=None):
        super().__init__(master)
        self.manager = InventoryManager()
        # Instancia el gestor de inventario para acceder a la lógica de negocio
        self._crear_widgets()
        # Crea los widgets de la interfaz y carga los clientes al iniciar la vista
        self._cargar_clientes()

    def _crear_widgets(self):
        # Frame para barra de búsqueda
        self.frame_busqueda = ttk.Frame(self)
        self.frame_busqueda.pack(fill=tk.X, padx=10, pady=(10,0))
        ttk.Label(self.frame_busqueda, text="Buscar por nombre:").pack(side=tk.LEFT)
        self.entry_busqueda = ttk.Entry(self.frame_busqueda)
        self.entry_busqueda.pack(side=tk.LEFT, padx=5)
        btn_buscar = ttk.Button(self.frame_busqueda, text="Buscar", command=self._filtrar_clientes)
        btn_buscar.pack(side=tk.LEFT)
        btn_limpiar = ttk.Button(self.frame_busqueda, text="Limpiar", command=self._limpiar_busqueda)
        btn_limpiar.pack(side=tk.LEFT, padx=5)
        # Frame de lista y botones
        # --- Tabla de clientes ---
        # Muestra la lista de clientes en formato de tabla
        self.frame_lista = ttk.Frame(self)
        self.frame_lista.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.tree = ttk.Treeview(self.frame_lista, columns=("ID", "Nombre", "Teléfono", "Email", "Dirección"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120)
        self.tree.pack(fill=tk.BOTH, expand=True)
        # --- Botones de acción ---
        # Permiten agregar y eliminar clientes
        self.frame_botones = ttk.Frame(self)
        self.frame_botones.pack(pady=10)
        self.btn_agregar = ttk.Button(self.frame_botones, text="Agregar cliente", command=self._abrir_agregar)
        self.btn_agregar.grid(row=0, column=0, padx=5)
        self.btn_eliminar = ttk.Button(self.frame_botones, text="Eliminar cliente", command=self._eliminar_cliente)
        self.btn_eliminar.grid(row=0, column=1, padx=5)
        
    def _filtrar_clientes(self):
        """
        Filtra los clientes por nombre según el texto de búsqueda ingresado en la barra.
        """
        texto = self.entry_busqueda.get().lower()
        todos = self.manager.listar_clientes()
        filtrados = [c for c in todos if texto in c.nombre_cliente.lower()]
        for item in self.tree.get_children():
            self.tree.delete(item)
        for c in filtrados:
            self.tree.insert("", tk.END, values=(c.id_cliente, c.nombre_cliente, c.telefono, c.email, c.direccion))

    def _limpiar_busqueda(self):
        """
        Limpia la barra de búsqueda y muestra la lista completa de clientes.
        """
        self.entry_busqueda.delete(0, tk.END)
        self._cargar_clientes()

    def _cargar_clientes(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        clientes = self.manager.listar_clientes()
        for c in clientes:
            self.tree.insert("", tk.END, values=(c.id_cliente, c.nombre_cliente, c.telefono, c.email, c.direccion))

    def _abrir_agregar(self):
        win = tk.Toplevel(self)
        win.title("Agregar cliente")
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
            Valida los datos ingresados y agrega el cliente si son correctos.
            """
            try:
                datos = [e.get() for e in entries]  # Obtiene los datos de los campos de entrada
                # Validación de ID (debe ser entero)
                if not datos[0].isdigit():
                    messagebox.showerror("Error", "El ID debe ser un número entero.")
                    return
                clientes_existentes = self.manager.listar_clientes()
                if any(c.id_cliente == int(datos[0]) for c in clientes_existentes):
                    messagebox.showerror("Error", f"El ID {datos[0]} ya existe para otro cliente.")
                    return
                datos[0] = int(datos[0])
                # Validación de teléfono (solo dígitos y longitud adecuada)
                if not validar_telefono(datos[2]):
                    messagebox.showerror("Error", "El número de teléfono no es válido. Debe contener solo dígitos y tener entre 7 y 15 caracteres.")
                    return
                # Validación de email (formato correcto)
                if not validar_email(datos[3]):
                    messagebox.showerror("Error", "El email no tiene un formato válido.")
                    return
                # Si todo es válido, agrega el cliente usando el gestor
                self.manager.agregar_cliente(*datos)
                messagebox.showinfo("Éxito", "Cliente agregado correctamente")
                win.destroy()
                self._cargar_clientes()
            except Exception as e:
                # Muestra un mensaje si ocurre un error inesperado
                messagebox.showerror("Error", f"No se pudo agregar el cliente: {e}")

        btn_guardar = ttk.Button(win, text="Guardar", command=guardar)
        btn_guardar.grid(row=len(labels), column=0, columnspan=2, pady=10)

    def _eliminar_cliente(self):
        """
        Elimina el cliente seleccionado de la tabla y la base de datos.
        """
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showwarning("Advertencia", "Seleccione un cliente para eliminar")
            return
        id_cliente = self.tree.item(seleccionado[0])["values"][0]
        self.manager.eliminar_cliente(id_cliente)
        self._cargar_clientes()
        messagebox.showinfo("Éxito", "Cliente eliminado")
