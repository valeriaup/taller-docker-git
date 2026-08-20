# Escenario 1 - Ejercicio: WordPress + MariaDB + phpMyAdmin

## Stack
- WordPress (últim versión)
- MariaDB 10.11 (en lugar de MySQL)
- phpMyAdmin para administrar la base de datos

## Cómo levantar el stack

1. Verifica que el archivo `.env` esté en esta misma carpeta con las variables configuradas.
2. Levanta los contenedores:
```bash
   docker-compose up -d
```
3. Accede a los servicios:
   - WordPress: http://localhost:8080
   - phpMyAdmin: http://localhost:8081

## Detener el stack

```bash
docker-compose down
```

Para eliminar también los volúmenes (borra todos los datos):
```bash
docker-compose down -v
```