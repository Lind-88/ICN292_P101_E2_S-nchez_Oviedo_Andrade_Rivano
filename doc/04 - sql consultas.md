# Consultas de negocio en MySQL

Las cinco consultas cubren movimientos registrados, compras por proveedor, gastos por categoría, medios de pago y control diario de pan. Los resultados corresponden a datos sintéticos del **24 de septiembre al 7 de octubre de 2026**. Los montos se expresan en pesos chilenos y las cantidades de pan en kilogramos.

Todas las consultas realizadas tienen de base un set de datos generados de manera artificial.

## 1. Ingresos y egresos registrados por mes

La consulta agrupa las ventas, las compras a proveedores y los gastos operacionales por mes. Usa `UNION ALL` para reunir los movimientos antes de sumar, conservando cada registro y evitando multiplicar montos cuando coinciden varias filas de la misma fecha.

| Período | Ingresos registrados | Egresos registrados | Diferencia registrada |
| ------- | -------------------: | ------------------: | --------------------: |
| 2026-09 |           $3.050.000 |          $2.214.000 |              $836.000 |
| 2026-10 |           $3.436.000 |          $2.536.500 |              $899.500 |

Ambos tramos tienen diferencia positiva. Septiembre cubre del 24 al 30 y octubre del 1 al 7. La diferencia considera solo ventas, facturas y gastos registrados en esos tramos. Para estimar utilidad o conciliar caja harían falta datos como costo de mercadería vendida, saldos y fechas efectivas de cobro y pago.

## 2. Compras por proveedor

La consulta cruza el catálogo de proveedores con las facturas. El `LEFT JOIN` conserva proveedores sin facturas, con conteo y total en cero.

| Proveedor | Facturas | Total de compras |
| --- | ---: | ---: |
| Proveedor ficticio A | 4 | $1.038.000 |
| Proveedor ficticio B | 3 | $546.000 |
| Proveedor ficticio C | 2 | $327.000 |
| Proveedor ficticio D | 2 | $306.000 |

El proveedor A concentra el 46,82 % de los $2.217.000 facturados en la muestra. El total y el número de facturas permiten identificar a quién revisar primero al contrastar compras con los respaldos.

## 3. Gastos por categoría

La consulta usa el catálogo de tipos de gasto para mostrar cada categoría, incluidas las categorías sin movimientos. El conteo usa el identificador del gasto y el total agrega el monto registrado.

| Categoría | Registros | Total |
| --- | ---: | ---: |
| Remuneraciones | 2 | $1.240.000 |
| Arriendo | 2 | $1.060.000 |
| Electricidad | 2 | $182.000 |
| Agua | 2 | $51.500 |

Remuneraciones y arriendo suman $2.300.000 de los $2.533.500 en gastos operacionales de la muestra. Las cuatro categorías tienen dos registros cada una. La diferencia de peso en el total se debe a sus montos.

## 4. Ventas por medio de pago

La consulta agrega los importes de los cierres diarios por medio de pago. El porcentaje de efectivo se calcula sobre el total de los tres medios y `NULLIF` evita dividir por cero cuando ese total es cero.

| Efectivo | Débito | Crédito | Efectivo sobre el total |
| ---: | ---: | ---: | ---: |
| $1.152.000 | $2.935.000 | $2.399.000 | 17,76 % |

El débito registra el mayor monto. La proporción de efectivo sirve para revisar la composición de las ventas de la muestra al contrastarla con los cierres diarios.

## 5. Serie diaria de compras y stock de pan

La consulta ordena por fecha los registros de `Flujo_Pan`.

| Fecha | Pan comprado (kg) | Stock al cierre (kg) |
| --- | ---: | ---: |
| 2026-09-24 | 24,00 | 3,00 |
| 2026-09-25 | 25,00 | 4,50 |
| 2026-09-26 | 26,00 | 6,00 |
| 2026-09-27 | 27,00 | 7,50 |
| 2026-09-28 | 28,00 | 3,00 |
| 2026-09-29 | 24,00 | 4,50 |
| 2026-09-30 | 25,00 | 6,00 |
| 2026-10-01 | 26,00 | 7,50 |
| 2026-10-02 | 27,00 | 3,00 |
| 2026-10-03 | 28,00 | 4,50 |
| 2026-10-04 | 24,00 | 6,00 |
| 2026-10-05 | 25,00 | 7,50 |
| 2026-10-06 | 26,00 | 3,00 |
| 2026-10-07 | 27,00 | 4,50 |

Hay 14 fechas consecutivas. En la muestra, las compras oscilan entre 24 y 28 kg y el stock al cierre entre 3 y 7,50 kg.
