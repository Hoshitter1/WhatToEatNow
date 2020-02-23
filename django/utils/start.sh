# Wait for db to be ready
sleep 5
# Get ready to create new db stuctures
python manage.py makemigrations
# reflect the changes on db
python manage.py migrate
# load initial data for admin
python manage.py loaddata init_user.json food_options.json
# run server for development (reflects file changes even while running server)
python manage.py runserver 0.0.0.0:8000

# run server for prosuction (This mode does not reflect changes)
#gunicorn what_to_eat_now.wsgi -b 0.0.0.0:8000"
