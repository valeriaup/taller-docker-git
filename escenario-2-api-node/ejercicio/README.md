# Escenario 2 - Ejercicio: API REST con CRUD completo + pgAdmin

## Stack
- Node.js + Express
- PostgreSQL 15
- pgAdmin (administración visual de la BD)

## Endpoints
- `GET /health` — estado del servicio
- `GET /usuarios` — lista todos los usuarios
- `GET /usuarios/:id` — obtiene un usuario
- `POST /usuarios` — crea un usuario (valida nombre y formato de email)
- `PUT /usuarios/:id` — actualiza un usuario
- `DELETE /usuarios/:id` — elimina un usuario

## Cómo levantar el stack

1. Verifica que el archivo `.env` esté en esta carpeta.
2. Levanta los contenedores:
```bash
   docker-compose up --build -d
```
3. Accede a los servicios:
   - API: http://localhost:3000
   - pgAdmin: http://localhost:5050 (login con las credenciales del `.env`)

## Conectar pgAdmin a la base de datos

1. Entra a pgAdmin con el email/password del `.env`.
2. Click derecho en "Servers" → "Register" → "Server".
3. En la pestaña "General", nombre: `API DB`.
4. En la pestaña "Connection":
   - Host: `db`
   - Port: `5432`
   - Database: valor de `DB_NAME` en `.env`
   - Username: valor de `DB_USER`
   - Password: valor de `DB_PASSWORD`

## Migrations

El script `init-scripts/01-init.sql` se ejecuta automáticamente la primera vez que se crea el volumen de PostgreSQL, creando la tabla `usuarios`.

## Detener el stack

```bash
docker-compose down
```

Para eliminar también los volúmenes (borra todos los datos):
```bash
docker-compose down -v
```