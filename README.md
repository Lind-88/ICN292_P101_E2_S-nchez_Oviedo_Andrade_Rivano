# SIG — Almacén La Maestra

**ICN292 — Sistemas de Información para la Gestión**  
**Universidad Técnica Federico Santa María**  
**Segundo semestre 2026 — Entrega 2**

## 1. Descripción del proyecto

Este proyecto consiste en el desarrollo de un Sistema de Información para la Gestión (SIG) para Almacén La Maestra, una PYME dedicada a la venta de productos de consumo diario, ubicada en Colina, Chile.

El objetivo es facilitar el registro, almacenamiento y consulta de información relacionada con las ventas diarias, compras a proveedores, gastos operacionales y control de compra de pan.

El sistema utiliza una base de datos MySQL y una aplicación desarrollada en Python. Adicionalmente, incorpora automatizaciones mediante n8n y notificaciones por Telegram para apoyar el control de registros y la reposición de pan.

## 2. Integrantes del equipo

- Juan Sánchez.
- Owen Oviedo.
- Camilo Rivano.
- Juan Andrade.

## 3. Funcionalidades principales

La aplicación permite:

- Registrar ventas diarias diferenciando efectivo, débito y crédito.
- Registrar compras a proveedores mediante facturas.
- Registrar gastos operacionales.
- Registrar cantidades compradas y stock de pan.
- Registrar proveedores y categorías de gastos.
- Consultar los últimos registros almacenados.
- Validar campos y evitar identificadores duplicados.

Además, se consideran dos automatizaciones:

**Nivel 1 Recordatorios:** consulta diariamente los registros existentes en MySQL y envía un resumen por Telegram, permitiendo identificar cierres o controles pendientes.

**Nivel 2 Reposición de pan:** consulta el historial almacenado en `Flujo_Pan`, estima el consumo aparente y calcula una cantidad sugerida de compra. El resultado se informa por Telegram para que el administrador tome la decisión final.

## 4. Tecnologías utilizadas

| Tecnología             | Función                                           |
| ---------------------- | ------------------------------------------------- |
| Python                 | Lenguaje utilizado para desarrollar la aplicación |
| Tkinter                | Interfaz gráfica de escritorio                    |
| MySQL Server           | Almacenamiento de información                     |
| MySQL Workbench        | Administración y ejecución de consultas SQL       |
| MySQL Connector/Python | Conexión entre Python y MySQL                     |
| n8n                    | Ejecución de automatizaciones                     |
| JavaScript             | Lógica de cálculo y procesamiento en n8n          |
| Telegram Bot API       | Envío de notificaciones al administrador          |
| GitHub                 | Repositorio y documentación del proyecto          |

## 5. Requisitos de instalación

Para ejecutar la solución se necesitan:

- Windows con Python 3 instalado.
- MySQL Server funcionando.
- MySQL Workbench, recomendado para configurar y verificar la base.
- Conexión a internet para instalar dependencias y enviar mensajes de Telegram.
- n8n instalado y funcionando, para utilizar las automatizaciones.
- Un bot de Telegram configurado.

### 5.1 Librerías de Python

La aplicación `SIG_La_Maestra.py` utiliza las siguientes bibliotecas:

| Biblioteca             | Uso                                | Instalación adicional |
| ---------------------- | ---------------------------------- | --------------------- |
| `tkinter`              | Ventanas, formularios y botones    | No                    |
| `tkinter.ttk`          | Componentes gráficos               | No                    |
| `tkinter.messagebox`   | Mensajes de confirmación y errores | No                    |
| `tkinter.simpledialog` | Solicitud de contraseña            | No                    |
| `datetime`             | Manejo de fechas                   | No                    |
| `decimal`              | Validación de montos y cantidades  | No                    |
| `mysql.connector`      | Conexión con MySQL                 | Sí                    |

La única dependencia externa es `mysql-connector-python`.

**Comando de instalación:**

`py -m pip install mysql-connector-python`

## 6. Instalación y ejecución del sistema

### Paso 1. Descargar el proyecto

Clonar el repositorio mediante Git o descargarlo como archivo ZIP desde GitHub.

Si se utiliza ZIP, descomprimirlo en una carpeta del computador.

### Paso 2. Instalar Python

Instalar Python 3 en Windows.

### Paso 3. Instalar el conector MySQL

En CMD, ejecutar:

`py -m pip install mysql-connector-python`

También se puede instalar desde un archivo `requirements.txt`:

`py -m pip install -r requirements.txt`

### Paso 4. Configurar MySQL

1. Iniciar MySQL Server.
2. Abrir MySQL Workbench.
3. Conectarse al servidor local.
4. Abrir el archivo `db/schema.sql`.
5. Ejecutar el script para crear la base de datos `ER` y sus tablas.

**Importante:** ejecutar `schema.sql` sobre un entorno limpio. Si la base `ER` ya existe, comprobar primero su estructura para evitar errores por tablas duplicadas. No eliminar una base con datos reales.

### Paso 5. Cargar datos de prueba

1. Abrir `db/seed.sql` en MySQL Workbench.
2. Ejecutar las instrucciones de inserción.
3. Comprobar que los registros se hayan cargado correctamente.

Los datos del archivo `seed.sql` son sintéticos y se utilizan exclusivamente para pruebas académicas.

### Paso 6. Comprobar las tablas

Ejecutar en MySQL Workbench:

```
USE ER;

SHOW TABLES;

SELECT * FROM Ventas_Diarias;
SELECT * FROM Compras_Proveedores;
SELECT * FROM Gasto_operacional;
SELECT * FROM Flujo_Pan;
SELECT * FROM Proveedor;
SELECT * FROM Tipo_de_gasto;
```

Deberán aparecer las seis tablas correspondientes al modelo ER.

### Paso 7. Ejecutar las consultas de negocio

1. Abrir el archivo `db/queries.sql`.
2. Ejecutar las consultas en MySQL Workbench.
3. Revisar los resultados.

Las consultas permiten analizar:

- Ingresos y egresos registrados por período.
- Compras agrupadas por proveedor.
- Gastos agrupados por categoría.
- Distribución de ventas por medio de pago.
- Evolución de las cantidades compradas y del stock de pan.

### Paso 8. Ejecutar la aplicación Python

Abrir mediante doble clic en `Abrir_SIG_La_Maestra.bat`, este abrirá `py SIG_La_Maestra.py`.

El programa solicitará la contraseña del usuario MySQL configurado.

La configuración actual utiliza:

- Servidor: `localhost`
- Puerto: `3306`
- Usuario: `root`
- Base de datos: `ER`

## 8. Uso de la aplicación

El menú principal permite seleccionar el tipo de información que se desea registrar.

### Ventas diarias

Se ingresa la fecha y los montos correspondientes a:

- Crédito.
- Débito.
- Efectivo.

El sistema calcula el total diario y guarda la información en `Ventas_Diarias`.

### Compras a proveedores

Se ingresa:

- Identificador de factura.
- Fecha.
- Monto total.
- Proveedor.

La información se almacena en `Compras_Proveedores`.

### Gastos operacionales

Se ingresa:

- Identificador del gasto.
- Fecha.
- Monto.
- Categoría.

Los datos quedan almacenados en `Gasto_operacional`.

### Control de pan

Se registra:

- Fecha.
- Cantidad de pan comprado.
- Stock de pan.

Los datos se almacenan en `Flujo_Pan`.

### Proveedores y categorías

La aplicación también permite registrar proveedores y categorías de gastos.

Estos registros se utilizan posteriormente en los formularios mediante listas desplegables.

## 9. Automatizaciones con n8n

Las automatizaciones utilizan los datos almacenados en MySQL y envían notificaciones mediante Telegram.

### Configuración inicial

1. Iniciar n8n.
2. Crear un workflow nuevo.
3. Seleccionar la opción **Import from File**.
4. Importar los archivos JSON correspondientes.
5. Configurar las credenciales MySQL.
6. Crear un bot mediante `@BotFather` en Telegram.
7. Obtener el token del bot y el Chat ID del destinatario.
8. Configurar las credenciales Telegram en n8n.
9. Revisar los horarios de ejecución y la zona horaria `America/Santiago`.
10. Guardar y activar/publicar los workflows.
