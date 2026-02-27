Nivel 1: Búsquedas Básicas
Obtén todas las series de la categoría 'Drama' que cuesten más de 15€.

Busca un director que sea 'Británico' usando .get(). (Maneja la excepción por si no existe).

Obtén las 2 series más antiguas estrenadas en la plataforma.

🟡 Nivel 2: Consultas Relacionadas y Objetos Q
Encuentra todos los Capítulos que pertenezcan a series dirigidas por "Vince Gilligan" (Usa el doble guion bajo __).

Busca series que cumplan una de estas dos condiciones: que el título contenga la palabra "Saul" O que su precio sea menor a 10€. (Usa objetos Q).

Excluye todas las series que sean de la categoría 'Sci-Fi' y ordénalas por nombre de forma descendente.

🟠 Nivel 3: Agregaciones y Anotaciones
Calcula el precio promedio de todas las series en la plataforma. (Usa aggregate).

Genera una lista de directores y, para cada uno, añade un campo llamado num_series que cuente cuántas series ha dirigido. (Usa annotate).

Obtén la serie que tenga el capítulo más largo de toda la base de datos. (Pista: Max).

🔴 Nivel 4: Optimización Profesional (N+1)
Escribe una consulta que obtenga todos los capítulos pero que, al acceder a capitulo.serie.director.nombre, no realice consultas adicionales a la base de datos. (Usa select_related encadenado).

Obtén todos los directores y precarga sus series para que, al listar sus títulos, el rendimiento sea óptimo. (Usa prefetch_related).