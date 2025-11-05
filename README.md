# 📦 Sistema de Gestión de Almacén

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![MySQL](https://img.shields.io/badge/MySQL-8.0+-orange.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

Sistema completo de gestión de inventario y almacén desarrollado en Python con interfaz gráfica Tkinter y base de datos MySQL. Permite la administración integral de productos, clientes, proveedores y movimientos de inventario.

## 🌟 Características

- **Gestión de Productos**: CRUD completo para productos con control de stock, precios, SKU y ubicaciones
- **Gestión de Clientes**: Administración de información de clientes con datos de contacto
- **Gestión de Proveedores**: Control de proveedores y sus datos de contacto
- **Registro de Movimientos**: Seguimiento de entradas y salidas de inventario con referencias y trazabilidad
- **Interfaz Gráfica Intuitiva**: Sistema de pestañas fácil de usar construido con Tkinter
- **Arquitectura Limpia**: Separación clara entre capas de datos, lógica de negocio y presentación

## 📋 Requisitos Previos

- Python 3.8 o superior
- MySQL Server 8.0 o superior
- pip (gestor de paquetes de Python)

## 🚀 Instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/ddani22/WarehouseManager.git
cd WarehouseManager
```

2. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

3. **Configurar la base de datos**

Crear un archivo `.env` en la raíz del proyecto con las credenciales de MySQL:
```env
DB_HOST=localhost
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña
DB_NAME=gestion_almacen
```

4. **Crear la base de datos**

Ejecutar el siguiente script SQL en MySQL:
```sql
CREATE DATABASE gestion_almacen;
USE gestion_almacen;

-- Tabla de proveedores
CREATE TABLE proveedores (
    id_proveedor INT PRIMARY KEY AUTO_INCREMENT,
    nombre_proveedor VARCHAR(100) NOT NULL,
    telefono VARCHAR(20),
    email VARCHAR(100),
    direccion TEXT
);

-- Tabla de productos
CREATE TABLE productos (
    id_producto INT PRIMARY KEY AUTO_INCREMENT,
    nombre_producto VARCHAR(100) NOT NULL,
    descripcion TEXT,
    sku VARCHAR(50) UNIQUE,
    precio_unitario DECIMAL(10,2),
    stock_actual INT DEFAULT 0,
    stock_minimo INT DEFAULT 0,
    ubicacion VARCHAR(50),
    id_proveedor INT,
    fecha_alta DATE,
    FOREIGN KEY (id_proveedor) REFERENCES proveedores(id_proveedor)
);

-- Tabla de clientes
CREATE TABLE clientes (
    id_cliente INT PRIMARY KEY AUTO_INCREMENT,
    nombre_cliente VARCHAR(100) NOT NULL,
    telefono VARCHAR(20),
    email VARCHAR(100),
    direccion TEXT
);

-- Tabla de movimientos
CREATE TABLE movimientos (
    id_movimiento INT PRIMARY KEY AUTO_INCREMENT,
    id_producto INT NOT NULL,
    tipo_movimiento ENUM('entrada', 'salida') NOT NULL,
    cantidad INT NOT NULL,
    fecha_movimiento DATETIME DEFAULT CURRENT_TIMESTAMP,
    referencia_origen VARCHAR(100),
    id_usuario INT,
    id_cliente_proveedor INT,
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
);
```

## 💻 Uso

Ejecutar la aplicación:
```bash
python src/app.py
```

La aplicación abrirá una ventana con cuatro pestañas principales:
- **Productos**: Gestión completa del catálogo de productos
- **Clientes**: Administración de clientes
- **Proveedores**: Control de proveedores
- **Movimientos**: Registro y seguimiento de movimientos de inventario

## 📁 Estructura del Proyecto

```
WarehouseManager/
│
├── src/
│   ├── app.py                 # Punto de entrada de la aplicación
│   ├── core/
│   │   └── inventory_manager.py  # Lógica de negocio principal
│   ├── database/
│   │   ├── db_manager.py      # Gestor de conexiones MySQL
│   │   └── dao/               # Data Access Objects
│   │       ├── productDAO.py
│   │       ├── clientDAO.py
│   │       ├── supplierDAO.py
│   │       └── movementDAO.py
│   ├── models/                # Modelos de datos
│   │   ├── product.py
│   │   ├── client.py
│   │   ├── supplier.py
│   │   └── movement.py
│   └── ui/                    # Interfaz gráfica
│       ├── main_window.py
│       ├── product_view.py
│       ├── client_view.py
│       ├── supplier_view.py
│       └── movement_view.py
│
├── tests/                     # Pruebas unitarias
│   ├── test_conexion_db.py
│   └── test_creacion_objetos.py
│
├── .env                       # Variables de entorno (no incluido en repo)
├── requirements.txt           # Dependencias del proyecto
└── README.md                  # Este archivo
```

## 🏗️ Arquitectura

El proyecto sigue una arquitectura en capas:

- **Capa de Presentación (UI)**: Interfaz gráfica con Tkinter
- **Capa de Lógica de Negocio (Core)**: `InventoryManager` coordina las operaciones
- **Capa de Acceso a Datos (DAO)**: Patrón DAO para operaciones CRUD
- **Capa de Modelos**: Entidades de dominio (Product, Client, Supplier, Movement)

### Patrón DAO

Cada entidad tiene su propio DAO que encapsula todas las operaciones de base de datos:
- `productDAO`: Operaciones CRUD para productos
- `clientDAO`: Operaciones CRUD para clientes
- `supplierDAO`: Operaciones CRUD para proveedores
- `movementDAO`: Operaciones CRUD para movimientos

## 🧪 Pruebas

Ejecutar las pruebas unitarias:
```bash
python -m unittest discover tests
```

## 🛠️ Tecnologías Utilizadas

- **Python 3.8+**: Lenguaje de programación principal
- **Tkinter**: Biblioteca para interfaz gráfica
- **MySQL Connector**: Conector de base de datos MySQL
- **python-dotenv**: Gestión de variables de entorno
- **MySQL 8.0+**: Sistema de gestión de base de datos

## 📝 Convenciones de Código

- Clases DAO utilizan lowercase (ej: `productDAO`, `clientDAO`)
- Modelos utilizan PascalCase (ej: `Product`, `Client`)
- Comentarios y docstrings en español
- Separación clara entre capas de la aplicación

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👤 Autor

**Daniel D.**

- GitHub: [@ddani22](https://github.com/ddani22)

## 🙏 Agradecimientos

Proyecto desarrollado como sistema de gestión empresarial para control de inventario y almacén.

---

⭐ Si este proyecto te ha sido útil, considera darle una estrella en GitHub
