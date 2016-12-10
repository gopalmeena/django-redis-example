In this code, I am using redis to store response of request. So when you will hit api for first time, it will get data from DB and will update cache with unique key.
Next time when you will hit on same api, whose response has been cached, now django will return response from redis. So there will be less load on DB or in short number of hits on DB has been reduced.


1. First Make Virtual Environment by "virtualenv <Your_Virtual_Environment_name>""
2. Now activate your virtual enironment by "source <Your_Virtual_Environment_name>/bin/activate"
3. Now change your  directory by "cd /res/""
4. Now install requirements to run this django-app by this command "pip install -r requirements.txt"
5. Now change your mysql password or mysql settings in  django-redis-example/res/locations/settings.py
6. Now go back to directory django-redis-example/res/
7. Run this command to make migrations "python manage.py makemigrations"
8. Now migrate those migrations by this command "python manage.py migrate"
9. Now run your application by "python manage.py runserver"
