run:
	python manage.py runserver 

makemig:
	python manage.py makemigrations

migrate:
	python manage.py migrate

freeze:
	pip freeze > requirements.txt

install:
	pip install -r requirements.txt

live:
	python manage.py livereload
