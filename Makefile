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
	cd __app__ && func start

.PHONY: dev
dev:
	cd __app__ && func azure functionapp publish $(DEV_ENV)

.PHONY: prod
prod:
	cd __app__ && func azure functionapp publish $(PROD_ENV)

