# Modelo de datos de Almacén La Maestra

La base MySQL `ER` guarda cierres diarios, compras a proveedores, gastos operacionales y el control diario de pan. Dos catálogos mantienen los datos de proveedores y categorías de gasto.

## Diccionario de datos

En las siguientes subsecciones se muestran las tablas para el modelo de datos, en donde PK identifica la clave primaria y FK la clave foránea.

De las tablas, un proveedor puede tener cero o muchas compras. Cada compra referencia a un proveedor existente. Una categoría puede tener cero o muchos gastos y cada gasto referencia a una categoría existente. Ventas y pan tienen registros diarios independientes. Las fechas de compras y gastos admiten varias filas por día.

## Tabla `Ventas_Diarias`

| Atributo           | Tipo            | Regla en SQL y significado                                          |
| ------------------ | --------------- | ------------------------------------------------------------------- |
| `Fecha`            | `DATE`          | PK. Una fila por fecha de cierre.                                   |
| `Monto_credito`    | `DECIMAL(12,1)` | Monto de ventas con crédito.                                        |
| `Monto_debito`     | `DECIMAL(12,1)` | Monto de ventas con débito.                                         |
| `Monto_efectivo`   | `DECIMAL(12,1)` | Monto de ventas en efectivo.                                        |

## Tabla `Compras_Proveedores`

| Atributo        | Tipo            | Regla en SQL y significado                  |
| --------------- | --------------- | ------------------------------------------- |
| `ID_factura`    | `VARCHAR(12)`   | PK. Identifica la factura de compra.        |
| `Monto_total`   | `DECIMAL(12,1)` | Importe de la factura.                      |
| `Fecha`         | `DATE`          | Obligatoria. Fecha de la compra.            |
| `rut_proveedor` | `VARCHAR(12)`   | FK obligatoria a `Proveedor.rut_proveedor`. |

## Tabla `Proveedor`

| Atributo           | Tipo           | Regla en SQL y significado          |
| ------------------ | -------------- | ----------------------------------- |
| `rut_proveedor`    | `VARCHAR(12)`  | PK. Identificador del proveedor.    |
| `nombre_proveedor` | `VARCHAR(100)` | Obligatorio. Nombre o razón social. |

## Tabla `Gasto_operacional`

| Atributo       | Tipo            | Regla en SQL y significado                     |
| -------------- | --------------- | ---------------------------------------------- |
| `ID_Gasto`     | `VARCHAR(12)`   | PK. Identifica el gasto.                       |
| `Fecha`        | `DATE`          | Obligatoria. Fecha del gasto.                  |
| `Monto_total`  | `DECIMAL(12,1)` | Importe del gasto.                             |
| `ID_Categoria` | `VARCHAR(12)`   | FK obligatoria a `Tipo_de_gasto.ID_Categoria`. |

## Tabla `Tipo_de_gasto`

| Atributo           | Tipo          | Regla en SQL y significado           |
| ------------------ | ------------- | ------------------------------------ |
| `ID_Categoria`     | `VARCHAR(12)` | PK. Identifica la categoría.         |
| `Nombre_Categoría` | `VARCHAR(50)` | Obligatorio. Nombre de la categoría. |

## Tabla `Flujo_Pan`

| Atributo       | Tipo           | Regla en SQL y significado                                          |
| -------------- | -------------- | ------------------------------------------------------------------- |
| `Fecha`        | `DATE`         | PK. Una fila por jornada de control.                                |
| `Pan_comprado` | `DECIMAL(6,2)` | Kilogramos comprados que el flujo atribuye a la jornada de la fila. |
| `Stock_pan`    | `DECIMAL(6,2)` | Kilogramos de pan remanente al cierre de esa jornada.               |

## Normalización y reglas de captura

- **Primera forma normal.** Cada campo contiene un valor y cada tabla tiene una clave primaria. Una fila representa una unidad definida, como una factura, un gasto o un cierre diario.
- **Segunda forma normal.** Las claves primarias tienen una columna. Los atributos dependen de la clave completa. Por ejemplo, la fecha y el importe de una factura dependen de `ID_factura`.
- **Tercera forma normal.** El nombre del proveedor depende de su RUT y se guarda en el catálogo `Proveedor`. El nombre de la categoría depende de su identificador y se guarda en `Tipo_de_gasto`. Los movimientos conservan las claves de referencia. El total diario de ventas se calcula sumando los medios de pago.

Los catálogos permiten registrar proveedores y categorías antes de que exista un movimiento, corregir un nombre en un solo registro y conservar la referencia aunque el catálogo tenga períodos sin movimientos. La separación de importes por medio de pago y el cálculo del total evitan discrepancias entre un total almacenado y sus componentes.

Las claves primarias impiden duplicados. Las claves foráneas exigen proveedor y categoría válidos para las compras y los gastos. La interfaz desarrollada [SIG_La_Maestra](SIG_La_Maestra.py) exige campos completos, montos y cantidades no negativos y los límites de decimales del diccionario. El esquema admite `NULL` en las columnas numéricas de importes y cantidades y delega esas comprobaciones de captura a la aplicación.

La interfaz [SIG_La_Maestra](SIG_La_Maestra.py), fue diseñada para ingresar los datos de manera mas sencilla por parte de usuarios que no manejen SQL.
