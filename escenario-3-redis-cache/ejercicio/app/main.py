from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import redis
import psycopg2
import psycopg2.extras
import os
import json

app = FastAPI(title="API Escenario 3 - Redis + PostgreSQL")

redis_client = redis.Redis(
    host=os.environ.get("REDIS_HOST", "redis"),
    port=int(os.environ.get("REDIS_PORT", 6379)),
    decode_responses=True
)

DB_CONFIG = {
    "host": os.environ.get("DB_HOST", "db"),
    "port": os.environ.get("DB_PORT", 5432),
    "user": os.environ.get("DB_USER", "postgres"),
    "password": os.environ.get("DB_PASSWORD", "postgres"),
    "dbname": os.environ.get("DB_NAME", "cachedb"),
}

def get_db_connection():
    return psycopg2.connect(**DB_CONFIG)

RATE_LIMIT_MAX = 10
RATE_LIMIT_WINDOW = 60  # segundos

@app.middleware("http")
async def rate_limit_middleware(request: Request, call_next):
    client_ip = request.client.host
    key = f"ratelimit:{client_ip}"

    current = redis_client.incr(key)
    if current == 1:
        redis_client.expire(key, RATE_LIMIT_WINDOW)

    if current > RATE_LIMIT_MAX:
        ttl = redis_client.ttl(key)
        return JSONResponse(
            status_code=429,
            content={
                "error": "Demasiadas solicitudes. Intenta de nuevo más tarde.",
                "retry_after_segundos": ttl
            }
        )

    return await call_next(request)

@app.get("/health")
def health():
    return {"status": "OK", "servicio": "FastAPI + Redis + PostgreSQL"}

@app.get("/contador")
def contador():
    total = redis_client.incr("contador_visitas")
    return {"contador_visitas": total}

@app.get("/usuarios")
def obtener_usuarios():
    cache_key = "usuarios_cache"
    datos_cache = redis_client.get(cache_key)
    if datos_cache:
        return {"origen": "cache", "usuarios": json.loads(datos_cache)}

    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute("SELECT id, nombre, email FROM usuarios ORDER BY id")
    usuarios = cur.fetchall()
    cur.close()
    conn.close()

    redis_client.setex(cache_key, 60, json.dumps(usuarios, default=str))

    return {"origen": "postgresql", "usuarios": usuarios}

@app.get("/cache/estadisticas")
def estadisticas_cache():
    info = redis_client.info()
    return {
        "keys_totales": redis_client.dbsize(),
        "memoria_usada": info.get("used_memory_human"),
        "hits": info.get("keyspace_hits"),
        "misses": info.get("keyspace_misses"),
    }

@app.get("/cache/limpiar")
def limpiar_cache():
    redis_client.flushdb()
    return {"mensaje": "Caché limpiada exitosamente"}