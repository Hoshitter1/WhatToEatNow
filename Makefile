
DB_USERNAME := user_dev
DB_NAME := develop_db
$(eval YOUR_CHANNEL_ACCESS_TOKEN := $(shell cat access_token_stg.txt))
$(eval YOUR_CHANNEL_SECRET := $(shell cat channel_secret_stg.txt))

database: #See what's in database
	docker exec -it postgres_db bash -c "psql -U $(DB_USERNAME) -d $(DB_NAME)"

web: #See what's in django
	docker-compose run django bash

ws: #See what's in webserver
	docker-compose run nginx bash

shell: #Going into django shell (Use this when debugging or when you forget your password and stuff)
	docker-compose run --rm django sh -c "sleep 1 && python /opt/apps/manage.py shell"

loaddata: #Read initial data
	docker-compose run --rm django sh -c "python manage.py loaddata init_user.json"

clean_db: #[BE CAREFUL] this deletes all migration history so that you can test various model structures
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete && find . -path "*/migrations/*.pyc"  -delete
	docker-compose down -v

build:
	docker-compose build --build-arg YOUR_CHANNEL_ACCESS_TOKEN=$(YOUR_CHANNEL_ACCESS_TOKEN) \
	                     --build-arg YOUR_CHANNEL_SECRET=$(YOUR_CHANNEL_SECRET)

debug:
	docker attach django_container
