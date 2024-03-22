to start the django app run 

To create a new django project run: 
```bash
 django-admin startproject mysite
```

```bash
poetry run python manage.py runserver
```
to add an app to this project run: 

```bash
poetry run python manage.py startapp <name_of_app>
```
then you must add the new app name inside the `INSTALLED_APPS` list found in the `settings.py` file found inside the project directory. (also include the urls in the main url file), this allows us to put specific logic inside specific applications 

will do the following now
[] If the query matches the name of an encyclopedia entry, the user should be redirected to that entry’s page.