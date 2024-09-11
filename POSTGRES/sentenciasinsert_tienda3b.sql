-- Active: 1725461045121@@127.0.0.1@5432@Tienda3B
INSERT INTO public.clientes (nombre, ap_paterno, direccion)
VALUES
('Juan', 'Pérez', 'Santiago, Región Metropolitana'),
('María', 'González', 'Valparaíso, Región de Valparaíso'),
('Carlos', 'López', 'Concepción, Región del Biobío'),
('Ana', 'Rodríguez', 'Antofagasta, Región de Antofagasta'),
('Pedro', 'Martínez', 'Temuco, Región de La Araucanía'),
('Luis', 'Fernández', 'Iquique, Región de Tarapacá'),
('Sofía', 'García', 'La Serena, Región de Coquimbo'),
('Ricardo', 'Vargas', 'Rancagua, Región de O’Higgins'),
('Marta', 'Hernández', 'Puerto Montt, Región de Los Lagos'),
('Laura', 'Torres', 'Punta Arenas, Región de Magallanes'),
('Diego', 'Silva', 'Arica, Región de Arica y Parinacota'),
('Elena', 'Morales', 'Copiapó, Región de Atacama'),
('Manuel', 'Castro', 'Talca, Región del Maule'),
('Paula', 'Méndez', 'Osorno, Región de Los Lagos'),
('José', 'Rojas', 'Chillán, Región de Ñuble'),
('Claudia', 'Ramírez', 'Valdivia, Región de Los Ríos'),
('David', 'Ortega', 'Curicó, Región del Maule'),
('Camila', 'Soto', 'Coyhaique, Región de Aysén'),
('Ángel', 'Núñez', 'Calama, Región de Antofagasta'),
('Valeria', 'Peña', 'Los Ángeles, Región del Biobío'),
('Gabriel', 'Suárez', 'Quillota, Región de Valparaíso'),
('Florencia', 'Navarro', 'San Antonio, Región de Valparaíso'),
('Esteban', 'Gutiérrez', 'Ovalle, Región de Coquimbo'),
('Natalia', 'Fuentes', 'Vallenar, Región de Atacama'),
('Santiago', 'Paredes', 'Talcahuano, Región del Biobío');

INSERT INTO public.productos (nombre, descripcion)
VALUES 
('Laptop', 'Laptop de 14 pulgadas con procesador Intel Core i7 y 16GB RAM'),
('Smartphone', 'Smartphone con pantalla OLED de 6.5 pulgadas y 128GB de almacenamiento'),
('Tablet', 'Tablet de 10 pulgadas con 64GB de almacenamiento y conexión Wi-Fi'),
('Smartwatch', 'Reloj inteligente con GPS y monitoreo de actividad física'),
('Cámara', 'Cámara digital con lente intercambiable de 24MP y 4K UHD'),
('Impresora 3D', 'Impresora 3D con tecnología FDM y cama caliente de 220x220mm'),
('Router Wi-Fi 6', 'Router de doble banda con soporte para Wi-Fi 6 y 3000Mbps'),
('Teclado Mecánico', 'Teclado mecánico con interruptores Cherry MX y retroiluminación RGB'),
('Monitor 4K', 'Monitor de 27 pulgadas con resolución 4K y tecnología HDR'),
('Mouse Gamer', 'Mouse gamer con 16.000 DPI y botones programables'),
('Audífonos Bluetooth', 'Audífonos inalámbricos con cancelación de ruido activa y 30 horas de batería'),
('Disco SSD', 'Disco sólido SSD de 1TB con conexión NVMe'),
('Tarjeta Gráfica', 'Tarjeta gráfica NVIDIA con 12GB de memoria GDDR6'),
('Placa Madre', 'Placa madre con soporte para procesadores AMD Ryzen y PCIe 4.0'),
('Memoria RAM', 'Memoria RAM DDR4 de 32GB a 3200MHz'),
('Fuente de Poder', 'Fuente de poder de 750W con certificación 80 PLUS Gold'),
('Gabinete Gaming', 'Gabinete ATX con panel lateral de vidrio templado y 4 ventiladores RGB'),
('Cámara Web', 'Cámara web con resolución Full HD y micrófono incorporado'),
('Parlantes Bluetooth', 'Parlantes portátiles con sonido estéreo y resistencia al agua IPX7'),
('Disco Duro Externo', 'Disco duro externo de 2TB con conexión USB 3.0'),
('Cargador Inalámbrico', 'Cargador inalámbrico Qi de 15W para dispositivos compatibles'),
('Microprocesador', 'Procesador AMD Ryzen 7 con 8 núcleos y 16 hilos'),
('Smart TV', 'Televisor inteligente de 55 pulgadas con resolución 4K UHD y sistema operativo Android'),
('Consola de Videojuegos', 'Consola de videojuegos de última generación con almacenamiento de 1TB'),
('Drone', 'Drone con cámara 4K, estabilizador de imagen y tiempo de vuelo de 30 minutos');

INSERT INTO public.tipo_transacciones (nombre, descripcion)
VALUES 
('Compra', 'Adquisición de productos'),
('Venta', 'Venta de productos a clientes'),
('Devolución', 'Devolución de productos adquiridos'),
('Garantía', 'Reemplazo o reparación de productos bajo garantía'),
('Cambio', 'Cambio de productos por otros'),
('Arrendamiento', 'Alquiler temporal de productos'),
('Reparación', 'Reparación de productos dañados'),
('Promoción', 'Compra con descuento o en oferta'),
('Suscripción', 'Suscripción a servicios relacionados con tecnología'),
('Donación', 'Donación de productos tecnológicos'),
('Upgrade', 'Actualización de componentes o productos'),
('Reembolso', 'Devolución de dinero por productos'),
('Mantenimiento', 'Mantenimiento de productos adquiridos'),
('Reserva', 'Reserva de productos antes de lanzamiento'),
('Intercambio', 'Intercambio de productos entre usuarios'),
('Renta', 'Renta de dispositivos electrónicos por tiempo limitado'),
('Subasta', 'Compra de productos mediante subasta'),
('Despacho', 'Servicio de despacho de productos'),
('Instalación', 'Servicio de instalación de productos tecnológicos'),
('Licencia', 'Compra de licencia de software'),
('Accesorios', 'Compra de accesorios para dispositivos'),
('Seguros', 'Seguro de dispositivos electrónicos'),
('Configuración', 'Servicio de configuración de productos'),
('Consultoría', 'Servicios de consultoría tecnológica'),
('Upgrade de Software', 'Actualización de software o sistemas operativos');

INSERT INTO public.transacciones (id_cliente, id_producto, id_tipo_transaccion, fecha, precio, cantidad)
VALUES 
(1, 1, 1, '2024-01-01', 1200.00, 1),
(2, 2, 1, '2024-01-02', 800.00, 1),
(3, 3, 2, '2024-01-03', 300.00, 2),
(4, 4, 1, '2024-01-04', 250.00, 1),
(5, 5, 4, '2024-01-05', 1100.00, 1),
(6, 6, 3, '2024-01-06', 600.00, 1),
(7, 7, 2, '2024-01-07', 150.00, 1),
(8, 8, 1, '2024-01-08', 450.00, 1),
(9, 9, 3, '2024-01-09', 700.00, 1),
(10, 10, 5, '2024-01-10', 70.00, 1),
(11, 11, 6, '2024-01-11', 90.00, 1),
(12, 12, 7, '2024-01-12', 1200.00, 1),
(13, 13, 8, '2024-01-13', 30.00, 3),
(14, 14, 9, '2024-01-14', 900.00, 1),
(15, 15, 10, '2024-01-15', 1100.00, 1),
(16, 16, 11, '2024-01-16', 600.00, 1),
(17, 17, 12, '2024-01-17', 450.00, 2),
(18, 18, 13, '2024-01-18', 350.00, 1),
(19, 19, 14, '2024-01-19', 800.00, 1),
(20, 20, 15, '2024-01-20', 250.00, 1),
(21, 21, 16, '2024-01-21', 600.00, 2),
(22, 22, 17, '2024-01-22', 1000.00, 1),
(23, 23, 18, '2024-01-23', 50.00, 1),
(24, 24, 19, '2024-01-24', 70.00, 2),
(25, 25, 20, '2024-01-25', 120.00, 1);

-- reporte de ventas por cliente
SELECT 
    c.id AS cliente_id,
    c.nombre AS nombre_cliente,
    c.ap_paterno AS apellido_cliente,
    SUM(t.cantidad) AS numero_ventas,
    SUM(t.precio * t.cantidad) AS total_ventas
FROM 
    public.transacciones t
JOIN 
    public.clientes c ON t.id_cliente = c.id
WHERE 
    t.id_tipo_transaccion = 2
GROUP BY 
    c.id, c.nombre, c.ap_paterno
ORDER BY 
    total_ventas DESC;

-- reporte de ventas por productos
SELECT 
    p.id AS producto_id,
    p.nombre AS nombre_producto,
    SUM(t.cantidad) AS total_vendido,
    SUM(t.precio * t.cantidad) AS ingresos_totales
FROM 
    public.transacciones t
JOIN 
    public.productos p ON t.id_producto = p.id
WHERE 
    t.id_tipo_transaccion = 2  -- Filtra solo las transacciones de tipo 'venta'
GROUP BY 
    p.id, p.nombre
ORDER BY 
    ingresos_totales DESC;
