### TEST
# ¯¯¯¯¯¯¯¯


test.create-container: ## Make testserver container if it doesn't exist
	docker-compose up --no-build --no-recreate testserver

.PHONY: test
test: test.create-container ## Launch tests in their own docker container
	docker-compose run --rm testserver

.PHONY: coverage
test.coverage: test.create-container  ## Generate test coverage
	docker-compose run --rm testserver bash -c "python -m pytest --cov-report term --cov-report html:coverage --cov-config setup.cfg --cov=src/ tests/"

.PHONY: lint
test.lint: test.create-container ## Lint python files with flake8
	docker-compose run --rm server bash -c "python -m flake8 ./src ./tests"
