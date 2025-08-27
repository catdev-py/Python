-- Agregar columna email en estudiantes
ALTER TABLE estudiantes
ADD COLUMN email VARCHAR(100);

-- Cambiar tipo de dato en curso
ALTER TABLE estudiantes
MODIFY COLUMN curso VARCHAR(100) NOT NULL;
