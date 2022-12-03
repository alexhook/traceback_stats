run:
	python3 traceback_stats/manage.py runserver

makemigrations:
	python3 traceback_stats/manage.py makemigrations

migrate:
	python3 traceback_stats/manage.py migrate
