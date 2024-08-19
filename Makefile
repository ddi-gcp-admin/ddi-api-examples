init:
	rm -rf .api_examples && python -m venv .api_examples
	. .api_examples/bin/activate
	pip install -r requirements.txt

authenticate:
	python authentication.py