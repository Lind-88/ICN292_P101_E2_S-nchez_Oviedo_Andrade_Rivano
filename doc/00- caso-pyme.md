# Caso PYME
La PYME en la que estamos trabajando se llama Almacen La Maestra, este es un almacen de barrio en Colina.   Para la entrega 2 seguimos trabajando con la misma PYME.

## Situación levantada en la Entrega 1.
Inicialmente el encargado realizaba los ingresos manualmente las ventas y egresos en una plantilla Excel.   Al ser registro manual, se podrian realizar errores o dejar campos incompletos.   Por otro lado, en el E1 se estimo que el trabajo de realizar la carga de datos en el excel requiere de 30 a 45 minutos de manera diaria.   Además, al ser un excel el cual posee muchas redundancias la forma de modificar datos o visualizarlos se dificultaba a la medida que agregaba más registros.

## Objetivos de la Entrega 2.
Al emplear una base de datos en SQL en vez de Excel se espera que el ingreso de datos se simplifique y se reduzca el riesgo de cometer errores.   Tambien se deberia de facilitar la forma en la que se consultara la información.   Se deberia reducir la cantidad de días en las que se omite la realización de los registros diarias y se realizaran sugerencias al momento de realizar la compra de pan.

| Necesidad del almacén | Solución propuesta en E2 |
| --- | --- |
| Consolidar ingresos y egresos| El registro de los ingresos se realizara diariamente desagregandose por medio de pago.   Los egresos se separan en dos: Gastos y compras a proveedores. |
| Revisar la actividad del período | Se extraera la información mediante consultas de SQL. |
| Detectar registros pendientes | La automatización de nivel 1 que se implementara sirve para recordar al encargado de realizar los registros diariamente mediante un mensaje de telegram. |
| Preparar el abastecimiento de pan | La automatización de nivel 2 que se realizara son recomendaciones diarias de la cantidad de pan a abastecer para el día siguiente.   Estas se basaran en el consumo promedio de los días anteriores y el stock disponible de pan.  Además estas sugerencias podrian ser aceptadas, ajustadas o descartadas por el encargado. |

