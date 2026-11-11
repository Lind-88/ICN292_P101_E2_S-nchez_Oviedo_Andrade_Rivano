CREATE DATABASE ER;
USE ER;


CREATE TABLE Ventas_Diarias (
Fecha date PRIMARY KEY,
Monto_credito decimal(12,1),
Monto_debito decimal(12,1),
Monto_efectivo decimal(12,1)
);

CREATE TABLE Compras_Proveedores (
ID_factura varchar(12) PRIMARY KEY,
Monto_total decimal(12,1),
Fecha date NOT NULL,
rut_proveedor varchar(12) NOT NULL
);

CREATE TABLE Proveedor (
rut_proveedor varchar(12) PRIMARY KEY,
nombre_proveedor varchar(100) NOT NULL
);

CREATE TABLE Flujo_Pan (
Fecha date PRIMARY KEY,
Pan_comprado decimal(6,2),
Stock_pan decimal(6,2)
);

CREATE TABLE Gasto_operacional (
ID_Gasto varchar(12) PRIMARY KEY,
Fecha date NOT NULL,
Monto_total decimal(12,1),
ID_Categoria varchar(12) NOT NULL
);

CREATE TABLE Tipo_de_gasto (
ID_Categoria varchar(12) PRIMARY KEY,
Nombre_Categoría varchar(50) NOT NULL
);

ALTER TABLE Compras_Proveedores ADD FOREIGN KEY (rut_proveedor) REFERENCES Proveedor (rut_proveedor);

ALTER TABLE Gasto_operacional ADD FOREIGN KEY (ID_Categoria) REFERENCES Tipo_de_gasto (ID_Categoria);
