# 01 - Requerimientos y evidencia de E2

Los requerimientos funcionales y los requerimientos no funcionales siguen la misma numeración que en la entrega 1.   Las prioridades siguen siendo las mismas que en la entrega inicial, ahora se tienen avances respecto a la primera entrega.

## Requerimientos funcionales
| ID | Prioridad E1 | Requerimiento | Evidencia y alcance en E2 |
| --- | --- | --- | --- |
| RF01 | Must have | El sistema debe de registrar las ventas diarias, considerando un monto total y los montos desagregados por método de pago. | El formulario registra crédito, débito y efectivo, y calcula el total.  Ventas_Diarias usa la fecha como clave primaria. |
| RF02 | Must have | El sistema debe registrar las compras a proveedores, considerando aspectos como fecha, proveedor y monto. | Compras_Proveedores registra identificador de factura, fecha, monto y proveedor. |
| RF03 | Must have | El sistema debe registrar los gastos operacionales, para posteriormente clasificarlos según el tipo de gasto operacional. | El formulario vincula cada gasto con una categoría del catálogo Tipo_de_gasto. |
| RF04 | Must have | El sistema debe permitir crear, editar y consultar proveedores, categorías y medios de pago. | La interfaz permite crear y visualizar proveedores y categorías. La edición quedó pendiente y los medios de pago de ventas están definidos en el formulario y en el esquema. |
| RF05 | Must have | El sistema debe permitir consultar y buscar información en los datos históricos. | La interfaz muestra hasta diez registros ordenados según la vista. Los scripts consultan datos históricos para el análisis. La búsqueda y los filtros en la interfaz quedaron pendientes. |
| RF06 | Must have | El sistema debe calcular indicadores de desempeño del periodo. | Hay cinco consultas SQL. Cubren diferencia mensual entre ingresos y egresos registrados, compras por proveedor, gastos por categoría, medios de pago y control de pan. Power BI se planteó en E1, pero para la entrega 2 se realizaran unicamente consultas de SQL. |
| RF07 | Should have | El sistema debe recordar al encargado realizar los registros diarios. | El Nivel 1 exportado programa un resumen a las 22:20 con el estado de cierres y pan y los conteos de facturas y gastos. |
| RF08 | Should have | El sistema debe de registrar la cantidad de pan abastecido y el stock disponible.| El formulario guarda los dos valores en kg en Flujo_Pan, con una fila por fecha. |
| RF09 | Should have | El sistema debe de realizar recomendaciones al encargado de las cantidades de pan a abastecer.| El Nivel 2 exportado estima consumo aparente y propone una cantidad cuando reúne historial suficiente. La decisión del encargado está modelada en BPMN. |

## Requerimientos no funcionales
| ID | Prioridad E1 | Requerimiento | Evidencia y alcance en E2 |
| --- | --- | --- | --- |
| RNF01 | Must have | El sistema debe ser fácilmente aprendible para los empleados del local y no debe de requerir conocimiento técnico especializado para emplearlo. | El menú separa los tipos de registro y los formularios indican formato, unidad y errores. |
| RNF02 | Must have | El sistema debe de guardar la información de manera permanente, de manera de que se mantengan disponibles en próximas instancias de uso. | El guardado confirma la transacción en MySQL. La reapertura con datos persistidos forma parte de la prueba operativa. |
| RNF03 | Should have | El sistema debe de permitir que usuarios que no posean conocimientos especializados sean capaces de configurar categorías y medios de pago. |  Hay un formulario para crear categorías. Los medios de pago de ventas son campos fijos. |
| RNF04 | Must have |  El sistema debe de permitir realizar los registros diarios en un bajo número de pasos. | El menú da acceso directo al formulario, que valida y guarda en una misma vista.  |
| RNF05 | Must have | El sistema debe de garantizar que la información ingresada cumpla con los formatos definidos y que no posea campos sin rellenar. | El formulario valida campos obligatorios, fechas, números, decimales y selección de catálogos. |
| RNF06 | Must have | El sistema debe de presentar los indicadores de desempeño de manera clara y comprensible para tomar de decisión. | Las consultas entregan la información de manera clara.  |


## Trazabilidad con la entrega 1

En la entrega 1 se propuso MySQL, n8n y PowerBI como arquitectura para la entrega 2.    En la entrega 2 se realizo el ingreso de datos mediante Python empleado Tkinter y efectivamente se uso n8n para las automatizaciones y MySQL para la arquitectura de la base de datos, pero para las consultas no se empleo PowerBI, si no que se emplearon las consultas del propio MySQL.
Durante la entrega 1 se definierón las estructuras y los procesos que se realizarían, por ejemplo los registros, recordatorios y sugerencias, y posteriormente en la entrega 2 se confeccionarón efectivamente las arquitecturas que permiten realizar los registros y consultas en la base de datos y la codificación de las automatizaciones que permiten sugerir el abastecimiento de pan y los recordatorios del registro diario de las ventas.

