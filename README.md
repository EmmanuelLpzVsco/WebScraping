# WebScraping
Scraping a tienda comercial, extracion de data, python3....


Este script realiza una solicitud GET al sitio web de Soriana con encabezados de usuario para evitar ser bloqueado, busca el menú de despensa y extrae la información de cada categoría y subcategoría. Finalmente, guarda la información en un archivo JSON. 
Me encontre con un leve de dificultad al hacer el llamado "request.get" el sitio neceita un encabezado para simular un navegador y un usuario para poder acc al sitio. Sin este no se puede acceder y la consulta se cuelga y nos regresa un codigo "403" por falta de autenticacion.
