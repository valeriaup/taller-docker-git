.PHONY: up down logs restart clean test

up:
	docker-compose up -d

build:
	docker-compose up --build -d

down:
	docker-compose down

clean:
	docker-compose down -v

logs:
	docker-compose logs -f

restart:
	docker-compose restart

ps:
	docker-compose ps

test:
	curl http://localhost:3000/health
	curl http://localhost:3000/usuarios