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
class AplicacionAlmacen:
    def __init__(self, ventana, password):
        self.ventana = ventana
        self.password = password

        self.ventana.title("SIG - Almacén La Maestra")
        self.ventana.geometry("900x680")
        self.ventana.minsize(760, 560)

        estilo = ttk.Style()
        if "clam" in estilo.theme_names():
            estilo.theme_use("clam")
        estilo.configure("Titulo.TLabel", font=("Arial", 19, "bold"))
        estilo.configure("Subtitulo.TLabel", font=("Arial", 10))
        estilo.configure("TButton", padding=8)
        estilo.configure("Treeview", rowheight=25)

        self.contenedor = ttk.Frame(self.ventana, padding=18)
        self.contenedor.pack(fill="both", expand=True)

        self.mostrar_menu()

    def conectar(self):
        """Se conecta a la base ER usando el mismo root de Workbench."""
        return mysql.connector.connect(
            host=HOST,
            port=PORT,
            user=USER,
            password=self.password,
            database=DATABASE,
            connection_timeout=5,
        )

    def ejecutar(self, consulta, parametros=(), obtener=False):
        conexion = self.conectar()
        cursor = conexion.cursor(dictionary=True)
        try:
            cursor.execute(consulta, parametros)
            if obtener:
                return cursor.fetchall()
            conexion.commit()
            return cursor.rowcount
        except Exception:
            conexion.rollback()
            raise
        finally:
            cursor.close()
            conexion.close()

    def limpiar(self):
        for elemento in self.contenedor.winfo_children():
            elemento.destroy()

    def encabezado(self, titulo, descripcion):
        ttk.Label(
            self.contenedor, text=titulo, style="Titulo.TLabel"
        ).pack(anchor="w", pady=(0, 5))
        ttk.Label(
            self.contenedor, text=descripcion, style="Subtitulo.TLabel",
            wraplength=820
        ).pack(anchor="w", pady=(0, 15))

    def mostrar_menu(self):
        self.limpiar()
        self.encabezado(
            "ALMACÉN LA MAESTRA",
            "Sistema sencillo para registrar ventas, compras, gastos y control de pan."
        )

        ttk.Label(
            self.contenedor,
            text="MENÚ PRINCIPAL",
            font=("Arial", 12, "bold")
        ).pack(anchor="w", pady=(5, 12))

        opciones = [
            "Ventas diarias",
            "Compras a proveedores",
            "Gastos operacionales",
            "Control de pan",
            "Registrar proveedores",
            "Registrar categorías",
        ]

        marco = ttk.Frame(self.contenedor)
        marco.pack(fill="x")

        for indice, nombre in enumerate(opciones):
            boton = ttk.Button(
                marco,
                text=nombre,
                command=lambda opcion=nombre: self.mostrar_formulario(opcion)
            )
            boton.grid(
                row=indice // 2,
                column=indice % 2,
                padx=7,
                pady=7,
                sticky="nsew",
                ipadx=12,
                ipady=12,
            )

        marco.columnconfigure(0, weight=1)
        marco.columnconfigure(1, weight=1)

        ttk.Separator(self.contenedor).pack(fill="x", pady=18)
        ttk.Label(
            self.contenedor,
            text="Los datos se guardan directamente en la base MySQL 'ER'.\n"
                 "Primero registra proveedores y categorías para poder seleccionarlos "
                 "en compras y gastos.",
            justify="left",
            wraplength=820,
        ).pack(anchor="w")

        ttk.Button(
            self.contenedor,
            text="Comprobar conexión con MySQL",
            command=self.comprobar_conexion
        ).pack(anchor="w", pady=(16, 0))

    def comprobar_conexion(self):
        try:
            filas = self.ejecutar("SELECT DATABASE() AS base", obtener=True)
            messagebox.showinfo(
                "Conexión correcta",
                "La aplicación está conectada a la base: " + str(filas[0]["base"])
            )
        except Exception as error:
            messagebox.showerror(
                "Error de conexión",
                "No se pudo conectar a MySQL.\n\n"
                "Comprueba que MySQL Server esté encendido y que la contraseña "
                "de root sea correcta.\n\nDetalle: " + str(error)
            )

    def obtener_opciones(self, tipo):
        if tipo == "proveedor":
            filas = self.ejecutar(
                "SELECT rut_proveedor, nombre_proveedor "
                "FROM Proveedor ORDER BY nombre_proveedor",
                obtener=True
            )
            return {
                f"{fila['nombre_proveedor']} ({fila['rut_proveedor']})":
                    fila["rut_proveedor"]
                for fila in filas
            }

        if tipo == "categoria":
            filas = self.ejecutar(
                "SELECT ID_Categoria, `Nombre_Categoría` "
                "FROM Tipo_de_gasto ORDER BY `Nombre_Categoría`",
                obtener=True
            )
            return {
                f"{fila['Nombre_Categoría']} ({fila['ID_Categoria']})":
                    fila["ID_Categoria"]
                for fila in filas
            }

        return {}

    def mostrar_formulario(self, nombre):
        datos = FORMULARIOS[nombre]
        self.limpiar()

        barra = ttk.Frame(self.contenedor)
        barra.pack(fill="x", pady=(0, 12))
        ttk.Button(
            barra, text="← Volver al menú", command=self.mostrar_menu
        ).pack(side="left")

        self.encabezado(nombre, "Completa los campos y presiona Guardar.")

        tarjeta = ttk.LabelFrame(
            self.contenedor, text="Datos del registro", padding=15
        )
        tarjeta.pack(fill="x", pady=(0, 15))

        controles = {}
        opciones = {}

        for indice, (columna, etiqueta, tipo) in enumerate(datos["campos"]):
            ttk.Label(tarjeta, text=etiqueta).grid(
                row=indice, column=0, sticky="w", padx=(0, 15), pady=7
            )

            if tipo in ("proveedor", "categoria"):
                try:
                    mapa = self.obtener_opciones(tipo)
                except Exception as error:
                    messagebox.showerror(
                        "No se pudieron cargar las opciones",
                        "Revisa la conexión MySQL.\n\n" + str(error)
                    )
                    self.mostrar_menu()
                    return

                opciones[columna] = mapa
                campo = ttk.Combobox(
                    tarjeta,
                    values=list(mapa.keys()),
                    state="readonly",
                    width=42
                )
                if mapa:
                    campo.current(0)
                else:
                    ttk.Label(
                        tarjeta,
                        text="No hay registros. Agrégalos desde el menú principal.",
                        foreground="darkred"
                    ).grid(row=indice, column=2, sticky="w", padx=8)
            else:
                campo = ttk.Entry(tarjeta, width=45)
                if tipo == "fecha":
                    campo.insert(0, date.today().isoformat())

            campo.grid(row=indice, column=1, sticky="ew", pady=7)
            controles[columna] = (campo, tipo)

        tarjeta.columnconfigure(1, weight=1)

        if nombre == "Ventas diarias":
            etiqueta_total = ttk.Label(
                tarjeta, text="Total del día: $0",
                font=("Arial", 11, "bold")
            )
            etiqueta_total.grid(
                row=len(datos["campos"]), column=1, sticky="w", pady=8
            )
            for columna in ("Monto_credito", "Monto_debito", "Monto_efectivo"):
                controles[columna][0].bind(
                    "<KeyRelease>",
                    lambda evento: self.actualizar_total(controles, etiqueta_total)
                )

        ttk.Button(
            tarjeta,
            text="GUARDAR",
            command=lambda: self.guardar(nombre, controles, opciones)
        ).grid(
            row=len(datos["campos"]) + 1,
            column=1,
            sticky="w",
            pady=(12, 4)
        )

        ttk.Label(
            self.contenedor,
            text="Últimos registros guardados",
            font=("Arial", 11, "bold")
        ).pack(anchor="w", pady=(4, 7))

        self.mostrar_registros(datos["tabla"], datos["orden"])

    def actualizar_total(self, controles, etiqueta):
        try:
            total = Decimal("0")
            for columna in ("Monto_credito", "Monto_debito", "Monto_efectivo"):
                texto = controles[columna][0].get().strip().replace(",", ".")
                if texto:
                    total += Decimal(texto)
            etiqueta.config(text=f"Total del día: ${total:,.1f}")
        except (InvalidOperation, ValueError):
            etiqueta.config(text="Total del día: revisa los montos")

    def convertir_valor(self, tipo, texto):
        valor = texto.strip()

        if not valor:
            raise ValueError("Completa todos los campos.")

        if tipo == "fecha":
            try:
                return date.fromisoformat(valor)
            except ValueError:
                raise ValueError("La fecha debe escribirse como AAAA-MM-DD.")

        if tipo in ("dinero", "cantidad"):
            try:
                numero = Decimal(valor.replace(",", "."))
            except InvalidOperation:
                raise ValueError("Ingresa un número válido. Ejemplo: 15000 o 2.50.")

            if not numero.is_finite() or numero < 0:
                raise ValueError("El monto o cantidad no puede ser negativo.")

            decimales = 1 if tipo == "dinero" else 2
            precision = Decimal("0.1") if decimales == 1 else Decimal("0.01")
            if numero != numero.quantize(precision):
                raise ValueError(
                    f"Se permiten como máximo {decimales} decimal(es)."
                )
            return numero

        if tipo == "id" and len(valor) > 12:
            raise ValueError("El identificador admite máximo 12 caracteres.")

        if tipo == "nombre100" and len(valor) > 100:
            raise ValueError("El nombre admite máximo 100 caracteres.")

        if tipo == "nombre50" and len(valor) > 50:
            raise ValueError("El nombre de categoría admite máximo 50 caracteres.")

        return valor

    def guardar(self, nombre, controles, opciones):
        datos = FORMULARIOS[nombre]
        valores = []

        try:
            for columna, etiqueta, tipo in datos["campos"]:
                texto = controles[columna][0].get()

                if tipo in ("proveedor", "categoria"):
                    mapa = opciones.get(columna, {})
                    if texto not in mapa:
                        raise ValueError(
                            "Primero debes registrar y seleccionar un "
                            + ("proveedor." if tipo == "proveedor" else "tipo de gasto.")
                        )
                    valor = mapa[texto]
                else:
                    valor = self.convertir_valor(tipo, texto)

                valores.append(valor)

            columnas_sql = ", ".join(f"`{columna}`" for columna in datos["columnas"])
            marcadores = ", ".join(["%s"] * len(datos["columnas"]))
            consulta = (
                f"INSERT INTO `{datos['tabla']}` "
                f"({columnas_sql}) VALUES ({marcadores})"
            )

            self.ejecutar(consulta, tuple(valores))

            messagebox.showinfo(
                "Registro guardado",
                "¡Listo! La información se guardó correctamente en MySQL."
            )
            self.mostrar_formulario(nombre)

        except MySQLError as error:
            codigo = getattr(error, "errno", None)

            if codigo == 1062:
                detalle = (
                    "Ya existe un registro con esa clave.\n"
                    "En ventas diarias y control de pan solo se permite "
                    "un registro por fecha."
                )
            elif codigo == 1452:
                detalle = (
                    "El proveedor o la categoría seleccionada no existe. "
                    "Vuelve al menú y revisa esos registros."
                )
            else:
                detalle = str(error)

            messagebox.showerror("No se pudo guardar", detalle)

        except (ValueError, InvalidOperation) as error:
            messagebox.showwarning("Revisa los datos", str(error))

        except Exception as error:
            messagebox.showerror("Error", str(error))

    def mostrar_registros(self, tabla, orden):
        try:
            filas = self.ejecutar(
                f"SELECT * FROM `{tabla}` ORDER BY `{orden}` DESC LIMIT 10",
                obtener=True
            )
        except Exception as error:
            ttk.Label(
                self.contenedor,
                text="No se pudieron mostrar los registros: " + str(error),
                wraplength=820
            ).pack(anchor="w")
            return

        if not filas:
            ttk.Label(
                self.contenedor,
                text="Todavía no hay registros en esta tabla."
            ).pack(anchor="w")
            return

        columnas = list(filas[0].keys())
        marco = ttk.Frame(self.contenedor)
        marco.pack(fill="both", expand=True)

        tabla_visual = ttk.Treeview(
            marco,
            columns=columnas,
            show="headings",
            height=8
        )
        barra = ttk.Scrollbar(
            marco, orient="vertical", command=tabla_visual.yview
        )
        tabla_visual.configure(yscrollcommand=barra.set)

        for columna in columnas:
            tabla_visual.heading(columna, text=columna)
            tabla_visual.column(
                columna, width=150, minwidth=100, anchor="center"
            )

        for fila in filas:
            tabla_visual.insert(
                "",
                "end",
                values=[
                    "" if fila[columna] is None else str(fila[columna])
                    for columna in columnas
                ]
            )

        tabla_visual.pack(side="left", fill="both", expand=True)
        barra.pack(side="right", fill="y")


def iniciar():
    ventana = tk.Tk()
    ventana.withdraw()

    if "mysql" not in globals() or mysql is None:
        messagebox.showerror(
            "Falta instalar un componente",
            "Primero instala el conector de MySQL.\n\n"
            "Abre CMD y ejecuta:\n"
            "py -m pip install mysql-connector-python"
        )
        ventana.destroy()
        return
    
    while True:
        password = simpledialog.askstring(
            "Conexión con MySQL",
            "Escribe la contraseña de tu usuario root de MySQL:\n"
            "(Si root no tiene contraseña, deja el espacio vacío.)",
            show="*",
            parent=ventana
        )

        if password is None:
            ventana.destroy()
            return

        try:
            conexion = mysql.connector.connect(
                host=HOST,
                port=PORT,
                user=USER,
                password=password,
                database=DATABASE,
                connection_timeout=5,
            )
            conexion.close()
            break

        except MySQLError as error:
            reintentar = messagebox.askretrycancel(
                "No se pudo conectar",
                "No fue posible conectarse a MySQL.\n\n"
                "Comprueba que MySQL Server esté encendido, que la base ER exista "
                "y que la contraseña sea correcta.\n\n"
                f"Detalle: {error}\n\n¿Quieres intentarlo otra vez?",
                parent=ventana
            )
            if not reintentar:
                ventana.destroy()
                return

    ventana.deiconify()
    AplicacionAlmacen(ventana, password)
    ventana.mainloop()


if __name__ == "__main__":
    iniciar()