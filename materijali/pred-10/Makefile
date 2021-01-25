export DOCKER_USER = $(shell id -u):$(shell id -g)
NUM_CPUS = $(shell nproc)


run: .env
	docker-compose up --build

.env: .env.example
	cp .env.example .env

scale.up:
	docker-compose scale worker=$(NUM_CPUS)

scale.down:
	docker-compose scale worker=1

reset:
	docker-compose down --volumes
	rm results/*.csv || true
