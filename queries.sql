USE ER;

WITH movimientos AS (
SELECT DATE_FORMAT(Fecha, '%Y-%m') AS periodo,
COALESCE(Monto_credito,0)+COALESCE(Monto_debito,0)+COALESCE(Monto_efectivo,0) AS ingreso,
0 AS egreso
FROM Ventas_Diarias
UNION ALL
SELECT DATE_FORMAT(Fecha, '%Y-%m'), 0, COALESCE(Monto_total,0)
FROM Compras_Proveedores
UNION ALL
SELECT DATE_FORMAT(Fecha, '%Y-%m'), 0, COALESCE(Monto_total,0)
FROM Gasto_operacional)
SELECT periodo,
ROUND(SUM(ingreso),1) AS ingresos_registrados,
ROUND(SUM(egreso),1) AS egresos_registrados,
ROUND(SUM(ingreso)-SUM(egreso),1) AS diferencia_registrada
FROM movimientos
GROUP BY periodo
ORDER BY periodo;

SELECT p.rut_proveedor,
p.nombre_proveedor,
COUNT(c.ID_factura) AS cantidad_facturas,
ROUND(COALESCE(SUM(c.Monto_total),0),1) AS total_compras
FROM Proveedor AS p
LEFT JOIN Compras_Proveedores AS c ON c.rut_proveedor=p.rut_proveedor
GROUP BY p.rut_proveedor,p.nombre_proveedor
ORDER BY total_compras DESC, p.nombre_proveedor;

SELECT t.ID_Categoria,
t.`Nombre_Categoría` AS categoria,
COUNT(g.ID_Gasto) AS cantidad_gastos,
ROUND(COALESCE(SUM(g.Monto_total),0),1) AS monto_total
FROM Tipo_de_gasto AS t
LEFT JOIN Gasto_operacional AS g ON g.ID_Categoria=t.ID_Categoria
GROUP BY t.ID_Categoria,t.`Nombre_Categoría`
ORDER BY monto_total DESC, categoria;

SELECT ROUND(SUM(COALESCE(Monto_efectivo,0)),1) AS total_efectivo,
ROUND(SUM(COALESCE(Monto_debito,0)),1) AS total_debito,
ROUND(SUM(COALESCE(Monto_credito,0)),1) AS total_credito,
ROUND(100.0*SUM(COALESCE(Monto_efectivo,0)) /
NULLIF(SUM(COALESCE(Monto_efectivo,0)+COALESCE(Monto_debito,0)+COALESCE(Monto_credito,0)),0),2)
AS porcentaje_efectivo
FROM Ventas_Diarias;

SELECT Fecha,Pan_comprado,Stock_pan
FROM Flujo_Pan
ORDER BY Fecha;