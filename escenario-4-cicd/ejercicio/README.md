# Escenario 4 - Ejercicio: CI/CD con Tests, Multi-stage, GHCR y Trivy

![CI/CD](https://github.com/valeriaup/taller-docker-git/actions/workflows/ci-cd.yml/badge.svg)

## Stack
- FastAPI (Python)
- Tests con pytest
- Docker multi-stage build
- GitHub Actions: test → build → scan (Trivy) → push (DockerHub + GHCR)

## Pipeline
1. **Test**: corre pytest sobre el código
2. **Build**: solo si los tests pasan
3. **Scan**: Trivy analiza vulnerabilidades CRITICAL/HIGH
4. **Push**: publica en DockerHub y GitHub Container Registry con tags semánticos

## Cómo levantar en desarrollo
```bash
docker-compose up --build -d
```

## Cómo levantar en producción (imagen ya publicada)
```bash
docker-compose -f docker-compose.prod.yml up -d
```

## Accesos
- API: http://localhost:8000
- Docs: http://localhost:8000/docs