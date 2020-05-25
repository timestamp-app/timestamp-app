DEV_ENV ?= devduck
PROD_ENV ?= wolfduck

.PHONY: lint
lint:
	pylint __app__

.PHONY: test
test:
	python -m unittest test/test_*

.PHONY: int_test
int_test:
	python -m unittest int_test/test_*

.PHONY: local
local:
	func start

.PHONY: dev
dev:
	func azure functionapp publish $(DEV_ENV)

.PHONY: prod
prod:
	func azure functionapp publish $(PROD_ENV)

