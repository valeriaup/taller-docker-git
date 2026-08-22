from fastapi import FastAPI

app = FastAPI(title="App CI/CD Ejercicio")

@app.get("/")
def index():
    return {
        "mensaje": "Hola desde FastAPI + CI/CD!",
        "version": "1.0.0"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}