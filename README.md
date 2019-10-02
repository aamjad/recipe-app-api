# recipe-app-api
Recipe app api source code


docker build .

docker-compose build

docker-compose run app sh -c "django-admin.py startproject app ."

git add .

git commit -m "comment"

git push origion

travis-ci.org

To test or run test cases
docker-compose run app sh -c "python manage.py test"


docker-compose run app sh -c "python manage.py startapp core"


docker-compose run app sh -c "python manage.py makemigrations core"
''' everytime you change the model, you need to run the migrations again


