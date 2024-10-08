-- Active: 1725461045121@@127.0.0.1@5432@ejemplos_having
-- This script was generated by the ERD tool in pgAdmin 4.
-- Please log an issue at https://github.com/pgadmin-org/pgadmin4/issues/new/choose if you find any bugs, including reproduction steps.
BEGIN;


CREATE TABLE IF NOT EXISTS public.proyectos
(
    id serial NOT NULL,
    descripcion text NOT NULL,
    id_cliente integer NOT NULL,
    id_estado integer NOT NULL,
    nombre_proyecto text NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.clientes
(
    id serial NOT NULL,
    nombre text NOT NULL,
    ap_paterno text NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.estado
(
    id serial NOT NULL,
    nombre text NOT NULL,
    descripcion text,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.proyecto_detalle
(
    id serial NOT NULL,
    id_proyecto integer NOT NULL,
    fecha_inicio date NOT NULL,
    fecha_termino date NOT NULL,
    presupuesto float NOT NULL,
    ubicacion text NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.empleados
(
    id serial NOT NULL,
    nombre text NOT NULL,
    ap_paterno text NOT NULL,
    id_cargo integer NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.cargos
(
    id serial NOT NULL,
    nombre text NOT NULL,
    descripcion text NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.empleado_contratacion
(
    id serial NOT NULL,
    fecha_contratacion date NOT NULL,
    fecha_termino date NOT NULL,
    salario float NOT NULL,
    id_empleado integer NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.proyecto_recursos_humanos
(
    id serial NOT NULL,
    id_empleado integer NOT NULL,
    id_proyecto integer NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.maquinarias
(
    id serial NOT NULL,
    nombre text NOT NULL,
    descripcion text NOT NULL,
    id_proyecto integer NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.materiales
(
    id serial NOT NULL,
    nombre text NOT NULL,
    descripcion text,
    id_proveedor integer NOT NULL,
    id_estado integer NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.material_detalle
(
    id serial NOT NULL,
    cantidad float NOT NULL,
    unidad_medida text,
    precio_compra float,
    id_material integer NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.proyectos_material
(
    id serial NOT NULL,
    id_proyecto integer NOT NULL,
    id_material integer NOT NULL,
    cantidad_material float NOT NULL,
    PRIMARY KEY (id)
);

ALTER TABLE IF EXISTS public.proyectos
    ADD FOREIGN KEY (id_cliente)
    REFERENCES public.clientes (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.proyectos
    ADD FOREIGN KEY (id_estado)
    REFERENCES public.estado (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.proyecto_detalle
    ADD FOREIGN KEY (id_proyecto)
    REFERENCES public.proyectos (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.empleados
    ADD FOREIGN KEY (id_cargo)
    REFERENCES public.cargos (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.empleado_contratacion
    ADD FOREIGN KEY (id_empleado)
    REFERENCES public.empleados (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.proyecto_recursos_humanos
    ADD FOREIGN KEY (id_proyecto)
    REFERENCES public.proyectos (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.proyecto_recursos_humanos
    ADD FOREIGN KEY (id_empleado)
    REFERENCES public.empleados (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.maquinarias
    ADD FOREIGN KEY (id_proyecto)
    REFERENCES public.proyectos (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.material_detalle
    ADD FOREIGN KEY (id_material)
    REFERENCES public.materiales (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.proyectos_material
    ADD FOREIGN KEY (id_proyecto)
    REFERENCES public.proyectos (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.proyectos_material
    ADD FOREIGN KEY (id_material)
    REFERENCES public.materiales (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;

INSERT INTO public.clientes (nombre, ap_paterno) VALUES
('Carlos', 'Pérez'),
('María', 'González'),
('Juan', 'López'),
('Carmen', 'Rojas'),
('Pedro', 'Hernández'),
('Francisca', 'Silva'),
('Roberto', 'Fuentes'),
('Patricia', 'Muñoz'),
('Jorge', 'Ramírez'),
('Sandra', 'Soto'),
('Raúl', 'Molina'),
('Isabel', 'Aravena'),
('Luis', 'Cáceres'),
('Claudia', 'Valenzuela'),
('Andrés', 'Morales');

INSERT INTO public.estado (nombre, descripcion) VALUES
('Iniciado', 'El proyecto ha comenzado'),
('En Proceso', 'El proyecto está en desarrollo'),
('Finalizado', 'El proyecto ha sido completado'),
('Cancelado', 'El proyecto ha sido cancelado');

INSERT INTO public.cargos (nombre, descripcion) VALUES
('Ingeniero', 'Ingeniero responsable del proyecto'),
('Arquitecto', 'Arquitecto encargado del diseño'),
('Obrero', 'Obrero que trabaja en la construcción'),
('Supervisor', 'Supervisor de obras');

INSERT INTO public.empleados (nombre, ap_paterno, id_cargo) VALUES
('Ana', 'Martínez', 1),  -- Ingeniero
('Pablo', 'Castro', 2),  -- Arquitecto
('Carlos', 'Soto', 3),   -- Obrero
('Lucía', 'Vargas', 4);  -- Supervisor

INSERT INTO public.proyectos (descripcion, id_cliente, id_estado, nombre_proyecto) VALUES
('Construcción de un edificio de oficinas', 1, 1, 'Edificio Corporativo'),
('Remodelación de una casa', 2, 2, 'Remodelación Casa González'),
('Construcción de un centro comercial', 3, 1, 'Centro Comercial López'),
('Proyecto de paisajismo', 4, 2, 'Jardín Rojas');

INSERT INTO public.proyectos (descripcion, id_cliente, id_estado, nombre_proyecto) VALUES
('Construcción de un edificio de oficinas', 1, 1, 'Edificio Corporativo'),
('Remodelación de una casa', 2, 2, 'Remodelación Casa González'),
('Construcción de un centro comercial', 3, 1, 'Centro Comercial López'),
('Proyecto de paisajismo', 4, 2, 'Jardín Rojas');

INSERT INTO public.proyecto_detalle (id_proyecto, fecha_inicio, fecha_termino, presupuesto, ubicacion) VALUES
('2024-01-15', '2024-12-15', 1000000, 'Santiago'),
('2024-02-10', '2024-07-30', 500000, 'Viña del Mar'),
('2024-03-01', '2025-01-01', 2000000, 'Concepción'),
('2024-04-20', '2024-09-20', 300000, 'Temuco');


END;