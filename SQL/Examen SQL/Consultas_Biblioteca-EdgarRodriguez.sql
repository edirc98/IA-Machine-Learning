-- DATOS DE LOS SOCIOS
select s.nombre as NOMBRE, s.telefono as TELEFONO, s.direccion as DIRECCION, s.DNI
from socios s;

-- SOCIOS REGISTRADOS EL 09/01/2021
select s.nombre as NOMBRE, s.telefono as TELEFONO, s.direccion as DIRECCION, s.DNI, s.fecha_registro as FECHA
from socios s
where fecha_registro like '2021-01-09';

-- LIBROS DE LA EDITORIAL PLESA
select l.titulo as TITULO, a.nombre as AUTOR ,l.año as AÑO, e.nombre as EDITORIAL
from libros l
join editoriales e on l.id_editorial = e.id
join autores a on l.id_autor = a.id
where e.nombre like 'Plesa';

-- EJEMPLARES QUE ESTAN DETERIORADOS
-- En la tabla de libro se muesra el deterioro con el campo con el mismo nombre
-- 0 si no hay deterioro, 1 se hay deterioro
select l.titulo as TITULO, a.nombre as AUTOR
from libros l 
join autores a on l.id_autor = a.id
where l.deterioro like '1';

-- LIBROS PRESTADOS A DIA DE HOY ( 26-02-2021)
select l.titulo as LIBRO, p.fecha_prestamo as FECHA, s.Nombre as NOMBRE, s.telefono as TELEFONO, s.DNI as DNI, s.direccion as DIR
from libros l
join prestamos p on l.id = p.id_libro
join socios s on p.id_socio = s.id
where fecha_prestamo like '2021-02-26';