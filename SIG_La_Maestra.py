import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from datetime import date
from decimal import Decimal, InvalidOperation

try:
    import mysql.connector
    from mysql.connector import Error as MySQLError
except ImportError:
    mysql = None
    MySQLError = Exception

HOST = "localhost"
PORT = 3306
USER = "root"
DATABASE = "ER"

FORMULARIOS = {
    "Ventas diarias": {
        "tabla": "Ventas_Diarias",
        "orden": "Fecha",
        "columnas": ["Fecha", "Monto_credito", "Monto_debito", "Monto_efectivo"],
        "campos": [
            ("Fecha", "Fecha (AAAA-MM-DD)", "fecha"),
            ("Monto_credito", "Monto crédito ($)", "dinero"),
            ("Monto_debito", "Monto débito ($)", "dinero"),
            ("Monto_efectivo", "Monto efectivo ($)", "dinero"),
        ],
    },
    "Compras a proveedores": {
        "tabla": "Compras_Proveedores",
        "orden": "Fecha",
        "columnas": ["ID_factura", "Monto_total", "Fecha", "rut_proveedor"],
        "campos": [
            ("ID_factura", "ID de factura (máximo 12 caracteres)", "id"),
            ("Monto_total", "Monto total ($)", "dinero"),
            ("Fecha", "Fecha (AAAA-MM-DD)", "fecha"),
            ("rut_proveedor", "Proveedor", "proveedor"),
        ],
    },
    "Gastos operacionales": {
        "tabla": "Gasto_operacional",
        "orden": "Fecha",
        "columnas": ["ID_Gasto", "Fecha", "Monto_total", "ID_Categoria"],
        "campos": [
            ("ID_Gasto", "ID del gasto (máximo 12 caracteres)", "id"),
            ("Fecha", "Fecha (AAAA-MM-DD)", "fecha"),
            ("Monto_total", "Monto total ($)", "dinero"),
            ("ID_Categoria", "Categoría", "categoria"),
        ],
    },
    "Control de pan": {
        "tabla": "Flujo_Pan",
        "orden": "Fecha",
        "columnas": ["Fecha", "Pan_comprado", "Stock_pan"],
        "campos": [
            ("Fecha", "Fecha (AAAA-MM-DD)", "fecha"),
            ("Pan_comprado", "Pan comprado (kg)", "cantidad"),
            ("Stock_pan", "Stock de pan (kg)", "cantidad"),
        ],
    },
    "Registrar proveedores": {
        "tabla": "Proveedor",
        "orden": "rut_proveedor",
        "columnas": ["rut_proveedor", "nombre_proveedor"],
        "campos": [
            ("rut_proveedor", "RUT del proveedor (máximo 12 caracteres)", "id"),
            ("nombre_proveedor", "Nombre del proveedor", "nombre100"),
        ],
    },
    "Registrar categorías": {
        "tabla": "Tipo_de_gasto",
        "orden": "ID_Categoria",
        "columnas": ["ID_Categoria", "Nombre_Categoría"],
        "campos": [
            ("ID_Categoria", "ID de categoría (máximo 12 caracteres)", "id"),
            ("Nombre_Categoría", "Nombre de categoría (máximo 50 caracteres)", "nombre50"),
        ],
    },
}