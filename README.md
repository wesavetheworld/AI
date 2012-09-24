# Article Intelligence 2.0

Switches platform to Django, adds tons of junk.  Hopefully isn't bad.

## Requirements

built for:

1.    django 1.4
2.    python 2.7.3

## Instructions

1.	git clone
2.	`cd .. ; virtualenv --no-site-packages env`
3.	`source env/bin/activate`
4.	`cd ai ; pip install -r requirements.txt`
5.	Setup mysql db if not already
6.	`python manage.py syncdb`
7.	(optional) `python manage.py loaddata < seed.json'
8.	`python manage.py runserver`


## testing

Run a bunch of tests with django's awesome unit testing framework:

`python manage.py test`

