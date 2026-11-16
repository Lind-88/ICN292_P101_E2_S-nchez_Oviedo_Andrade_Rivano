# BPMN To-Be de Almacén La Maestra

El modelo E2 conecta el registro diario del almacén con el control de información y la planificación de la compra de pan. El personal captura los datos en el SIG, MySQL los conserva, n8n consulta la base y envía los avisos por Telegram, y el encargado decide cómo actuar.

## Diagrama y archivos

En Bizagi Modeler, abre [BPMN.bpm](assest/BPMN.bpm).

## Participantes y traspasos

| Participante o carril | Actividad | Resultado |
| --- | --- | --- |
| Trabajador o administrador | Ingresa el registro en el formulario y corrige los campos cuando la aplicación informa un error de validación. | Datos de cierre, compra, gasto o control de pan listos para guardar. |
| SIG en Python/Tkinter | Valida los datos e intenta insertar el registro en MySQL. | Confirmación de guardado o mensaje de error. |
| Automatización n8n, nivel 1 | A las 22:20 consulta los registros del día, prepara el resumen y lo envía por Telegram. | El encargado recibe el estado del cierre, control de pan, facturas y gastos. |
| Automatización n8n, nivel 2 | A las 08:00, 18:00 y 22:00 verifica si corresponde avisar, estima el consumo con el historial y envía una sugerencia o un aviso de historial insuficiente. | El encargado recibe la información para decidir. El flujo marca la fecha después del envío. |
| Encargado de revisión | Revisa el resumen y completa registros cuando corresponde. Evalúa el aviso de pan y aprueba, ajusta o define manualmente, o rechaza la compra. | Revisión completada y decisión de compra bajo responsabilidad del almacén. |

## Cambios desde E1

| Aspecto | E1 | E2 |
| --- | --- | --- |
| Captura y validación | El To-Be separaba el cierre de caja y los egresos, con validación y retorno para corregir. | La aplicación concreta el ingreso y la validación en Tkinter, y el registro en MySQL. El control de pan tiene su propio registro diario. |
| Revisión de registros | Se planteaban revisiones y recordatorios de ingresos y egresos en el carril SIG. | El nivel 1 reúne el estado de cuatro tipos de registro en un resumen a las 22:20 y deja explícita la revisión del encargado. |
| Reposición de pan | Se consultaba el historial, se solicitaba el stock y se enviaba una recomendación al dueño. | El nivel 2 consulta `Flujo_Pan` en horarios definidos. Las ramas distinguen entre una sugerencia, historial insuficiente y una ejecución sin aviso. El BPMN explicita las decisiones del encargado. |
| Responsabilidades | El carril SIG concentraba la lógica automatizada del modelo conceptual. | El participante n8n identifica los dos niveles y los mensajes de Telegram. La captura, la persistencia y la decisión quedan asociadas a sus responsables. |

