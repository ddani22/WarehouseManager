# Modelo de producto
class Product:
    """
    Modelo que representa un producto en el sistema de gestión de almacén.
    """
    def __init__(self, id_producto, nombre_producto, descripcion, sku, precio_unitario, stok_actual, stock_minimo, ubicacion, id_proveedor, fecha_alta):
        """
        Inicializa un nuevo producto.
        :param id_producto: int, identificador único del producto
        :param nombre_producto: str, nombre del producto
        :param descripcion: str, descripción del producto
        :param precio: float, precio del producto
        :param cantidad_stock: int, cantidad disponible en stock
        """
        self.id_producto = id_producto
        self.nombre_producto = nombre_producto
        self.descripcion = descripcion
        self.sku = sku
        self.precio_unitario = precio_unitario
        self.stock_actual = stok_actual
        self.stock_minimo = stock_minimo 
        self.ubicacion = ubicacion
        self.id_proveedor = id_proveedor
        self.fecha_alta = fecha_alta

    def __str__(self):
        """
        Devuelve una representación en cadena del producto.
        """
        return f"Producto({self.id_producto}, {self.nombre_producto}, {self.descripcion}, {self.sku}, {self.precio_unitario}, {self.stock_actual}, {self.stock_minimo}, {self.ubicacion}, {self.id_proveedor}, {self.fecha_alta})"