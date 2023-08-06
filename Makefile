dev:
	poetry run python3 manage.py runserver

venv:
	source $(poetry env info --path)/bin/activate

shell:
	poetry run python manage.py shell