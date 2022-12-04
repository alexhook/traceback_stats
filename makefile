run:
	python3 -m traceback_stats.manage runserver

collectstatic:
	python3 -m traceback_stats.manage collectstatic

makemigrations:
	python3 -m traceback_stats.manage makemigrations

migrate:
	python3 -m traceback_stats.manage migrate

createsuperuser:
	python3 -m traceback_stats.manage createsuperuser
