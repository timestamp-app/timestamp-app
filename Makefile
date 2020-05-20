.PHONY: lint
lint:
	pylint datainput htmlgenerator

.PHONY: test
test:
	python -m unittest

.PHONY: local
local:
	func start

