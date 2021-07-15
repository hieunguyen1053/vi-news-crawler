clean: clean-pycache clean-ds

clean-ds:
	find . -name ".DS_Store" -delete

clean-pycache:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-small-data:
	find 'data' -name "*.json" -type 'f' -size -1k -delete

compress-data: clean-small-data
	tar -czvf compress/`date +%F`.zip data