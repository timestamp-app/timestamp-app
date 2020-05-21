MODULES = datainput htmlgenerator helpers
DEV_ENV ?= devduck
PROD_ENV ?= wolfduck

.PHONY: lint
lint:
	pylint $(MODULES)

.PHONY: test
test:
	python -m unittest

.PHONY: local
local:
	func start

.PHONY: dev
dev:
	func azure functionapp publish $(DEV_ENV)

.PHONY: prod
prod:
	func azure functionapp publish $(PROD_ENV)

