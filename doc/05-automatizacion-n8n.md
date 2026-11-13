# Automatización n8n de Almacén La Maestra

Los dos flujos programados consultan MySQL y entregan avisos al encargado del almacén por Telegram. La captura se realiza en la aplicación Tkinter y la decisión de compra se toma manualmente.

## Configuración de la demostración

1. Crea la base `ER` y carga los datos de demostración siguiendo el [README](../README.md).
2. Importa en n8n los JSON de nivel 1 y nivel 2. Ambos están exportados inactivos.
3. Configura una credencial MySQL con acceso de lectura a `ER` desde la instancia de n8n y asígnala a los dos nodos MySQL. Configura la credencial del bot de Telegram y reemplaza `REEMPLAZAR_CHAT_ID` en los nodos de envío por el chat de prueba. Mantén las credenciales en n8n.
4. Configura la zona horaria de los flujos en `America/Santiago` y comprueba que la sesión de MySQL use la misma fecha local. Los nodos SQL usan `CURRENT_DATE()` o `CURDATE()` para seleccionar registros.
5. Para probar los mensajes de hoy, utiliza registros fechados hoy en una base de prueba. La semilla utiliza fechas históricas del 24 de septiembre al 7 de octubre de 2026. Para repetir ese período, cambia la fecha de referencia en copias de prueba de las consultas. Activa los flujos cuando estén configurados para comprobar la ejecución programada.

## Nivel 1 - Resumen diario

En el BPMN, este flujo corresponde a "Enviar resumen por Telegram".

| Paso | Nodo de n8n                 | Qué hace                                                                                                         |
| ---- | --------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| 1    | Cada dia a las 22:20        | Dispara el flujo todos los días a las 22:20.                                                                     |
| 2    | Leer estado de registros ER | Cuenta las filas de hoy en `Ventas_Diarias`, `Compras_Proveedores`, `Gasto_operacional` y `Flujo_Pan`.           |
| 3    | Preparar recordatorio       | Indica si están registrados el cierre de ventas y el control de pan, y muestra los conteos de facturas y gastos. |
| 4    | Enviar resumen por Telegram | Envía el mensaje al chat configurado para que el encargado revise los registros.                                 |

Si no hay cierre o control de pan, el mensaje avisa que falta el registro del día. Cero facturas o gastos es un dato para revisar, porque puede corresponder a una jornada sin esos movimientos. El resumen informa presencia y conteos de registros.

## Nivel 2 - Reposición de pan

En el BPMN, este flujo corresponde a "Enviar aviso de pan por Telegram".

| Paso | Nodo de n8n                       | Qué hace                                                                                                                              |
| ---- | --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| 1    | Revisar MySQL                     | Ejecuta el flujo a las 08:00, 18:00 y 22:00.                                                                                          |
| 2    | Buscar registro de pan del dia    | Si existe una fila de hoy, consulta `Flujo_Pan` desde hoy menos 14 días hasta hoy, ambas fechas incluidas.                            |
| 3    | Calcular sugerencia para Telegram | Comprueba la fecha y los datos, evita repetir una fecha marcada y calcula la sugerencia o prepara el aviso de historial insuficiente. |
| 4    | Enviar sugerencia por Telegram    | Envía la sugerencia o el aviso al encargado.                                                                                          |
| 5    | Marcar fecha notificada           | Después del envío, guarda la fecha en el estado del flujo para omitir revisiones posteriores de la misma jornada.                     |
