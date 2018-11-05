# Destacame's evaluation
* Python 3.6.0

## Documentation
https://drive.google.com/open?id=1yUZ-VncTulc3bpbtpG2N22GBETHdO1pk


## Instalation
```
pip install -r requirements.txt
```


### Commands
* Run app:
```
python manage.py runserver 0.0.0.0:8000
```

* Run Test:
```
python manage.py test passenger.tests
```

* Run migration:
```
python manage.py migrate --settings=settings.dev
```

* fixtures
```
python manage.py loaddata app/driver/fixtures/0001_initial.json
python manage.py loaddata app/passenger/fixtures/0001_initial.json
python manage.py loaddata app/bus/fixtures/0001_initial.json
```


### Tecnología
* [Django] - Framework de Python
* [Graphql] - A query language for your API

[Django]:https://www.djangoproject.com/
[Graphql]:https://graphql.org/
