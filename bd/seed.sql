USE ER;

INSERT INTO Proveedor (rut_proveedor, nombre_proveedor) VALUES
  ('DEMO-P001', 'Proveedor ficticio A'),
  ('DEMO-P002', 'Proveedor ficticio B'),
  ('DEMO-P003', 'Proveedor ficticio C'),
  ('DEMO-P004', 'Proveedor ficticio D');

INSERT INTO Tipo_de_gasto (ID_Categoria, `Nombre_Categoría`) VALUES
  ('CAT-01', 'Arriendo'),
  ('CAT-02', 'Electricidad'),
  ('CAT-03', 'Agua'),
  ('CAT-04', 'Remuneraciones');

INSERT INTO Ventas_Diarias (Fecha, Monto_credito, Monto_debito, Monto_efectivo) VALUES
  ('2026-09-24', 120000, 175000, 78000),
  ('2026-09-25', 150000, 168000, 55000),
  ('2026-09-26', 210000, 230000, 82000),
  ('2026-09-27', 193000, 240000, 93000),
  ('2026-09-28', 154000, 186000, 65000),
  ('2026-09-29', 135000, 190000, 64000),
  ('2026-09-30', 170000, 204000, 88000),
  ('2026-10-01', 160000, 210000, 70000),
  ('2026-10-02', 145000, 199000, 82000),
  ('2026-10-03', 235000, 260000, 104000),
  ('2026-10-04', 225000, 245000, 112000),
  ('2026-10-05', 180000, 220000, 96000),
  ('2026-10-06', 147000, 193000, 73000),
  ('2026-10-07', 175000, 215000, 90000);

INSERT INTO Compras_Proveedores (ID_factura, Monto_total, Fecha, rut_proveedor) VALUES
  ('FAC-DEMO-01', 215000, '2026-09-24', 'DEMO-P001'),
  ('FAC-DEMO-02', 176000, '2026-09-25', 'DEMO-P002'),
  ('FAC-DEMO-03', 185000, '2026-09-27', 'DEMO-P003'),
  ('FAC-DEMO-04', 268000, '2026-09-29', 'DEMO-P001'),
  ('FAC-DEMO-05', 111000, '2026-09-30', 'DEMO-P004'),
  ('FAC-DEMO-06', 265000, '2026-10-01', 'DEMO-P001'),
  ('FAC-DEMO-07', 185000, '2026-10-02', 'DEMO-P002'),
  ('FAC-DEMO-08', 142000, '2026-10-03', 'DEMO-P003'),
  ('FAC-DEMO-09', 195000, '2026-10-04', 'DEMO-P004'),
  ('FAC-DEMO-10', 290000, '2026-10-06', 'DEMO-P001'),
  ('FAC-DEMO-11', 185000, '2026-10-07', 'DEMO-P002');

INSERT INTO Gasto_operacional (ID_Gasto, Fecha, Monto_total, ID_Categoria) VALUES
  ('GO-DEMO-01', '2026-09-24', 85000, 'CAT-02'),
  ('GO-DEMO-02', '2026-09-25', 24000, 'CAT-03'),
  ('GO-DEMO-03', '2026-09-28', 530000, 'CAT-01'),
  ('GO-DEMO-04', '2026-09-30', 620000, 'CAT-04'),
  ('GO-DEMO-05', '2026-10-01', 97000, 'CAT-02'),
  ('GO-DEMO-06', '2026-10-03', 27500, 'CAT-03'),
  ('GO-DEMO-07', '2026-10-05', 530000, 'CAT-01'),
  ('GO-DEMO-08', '2026-10-07', 620000, 'CAT-04');

INSERT INTO Flujo_Pan (Fecha, Pan_comprado, Stock_pan) VALUES
  ('2026-09-24', 24.0, 3.0),
  ('2026-09-25', 25.0, 4.5),
  ('2026-09-26', 26.0, 6.0),
  ('2026-09-27', 27.0, 7.5),
  ('2026-09-28', 28.0, 3.0),
  ('2026-09-29', 24.0, 4.5),
  ('2026-09-30', 25.0, 6.0),
  ('2026-10-01', 26.0, 7.5),
  ('2026-10-02', 27.0, 3.0),
  ('2026-10-03', 28.0, 4.5),
  ('2026-10-04', 24.0, 6.0),
  ('2026-10-05', 25.0, 7.5),
  ('2026-10-06', 26.0, 3.0),
  ('2026-10-07', 27.0, 4.5);
