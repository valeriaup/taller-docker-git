# Escenario 3 - Ejercicio: FastAPI + Redis + PostgreSQL

## Stack
- FastAPI (en lugar de Flask)
- Redis (caché + rate limiting + contador)
- PostgreSQL (fuente de verdad)

## Endpoints
- `GET /health`
- `GET /contador` — incrementa y devuelve un contador de visitas (Redis INCR)
- `GET /usuarios` — primero busca en Redis, si no está, consulta PostgreSQL y cachea
- `GET /cache/estadisticas`
- `GET /cache/limpiar`

## Rate limiting
Máximo 10 requests por minuto por IP. Al superarlo, responde `429` con el tiempo restante.

## Cómo levantar (desarrollo, con hot-reload)
```bash
docker-compose up --build -d
```
Docker Compose toma automáticamente `docker-compose.yml` + `docker-compose.override.yml`.

## Cómo levantar (producción, sin override)
```bash
docker-compose -f docker-compose.yml up --build -d
```

## Accesos
- API: http://localhost:8000
- Docs interactivas (Swagger): http://localhost:8000/docs
- PostgreSQL: puerto 5434
- Redis: puerto 6380

## Detener
```bash
docker-compose down
```