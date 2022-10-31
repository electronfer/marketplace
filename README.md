# [Step 1] Start the project
```
django-admin startproject <project name>
```

# [Step 2] Run server
```
python manage.py runserver
```

# [Step 3] Create some app
```
python manage.py startapp <app name>
```

# [Step 4] Create some app
Create the file **urls.py** in the app directory

# [Step 5] Database configuration
## Install PosgreSQL
```
pip install psycopg2
```
## Preparing django to create tables or updates tables using the ORM for the specific application 
```
python manage.py makemigrations <app name>
```
or all the apps
```
python manage.py makemigrations
```

## Run the migrations to apply those changes to the database
```
python manage.py migrate
```

## To validate the SQL commands performed in the migrations, we run the following command
```
python manage.py sqlmigrate <app name> <migration number>
```

# Open the interactive Python shell and play around with the free API Django
```
python manage.py shell
```

# Creation of superuser
```
python manage.py createsuperuser
```