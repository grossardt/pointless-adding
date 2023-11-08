.PHONY: lint test html clean

lint:
	python -m pylint -rn pointless_adding test

test:
	python -m unittest discover -v test

html:
	sphinx-build -M html docs docs/_build -W -T --keep-going

clean:
	make -C docs clean
