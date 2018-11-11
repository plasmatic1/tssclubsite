# tssclubsite

A WIP club/announcements backend for schools.

Made using Django 2.1.3.

Main contributor(s): 

* [Jonathan Sumabat](https://github.com/jsumabat)

## Installed Applications

You will need [sortedm2m](https://github.com/gregmuellegger/django-sortedm2m) in order for some pages to work properly. Furthermore, I recommend to delete the migrations and reset them through the following steps:

1. Delete everything in the `club_management/migrations` folder with the exception of `__init.py__`.
2. Run `python manage.py makemigrations`
3. Run `python manage.py migrate`
4. The application should run perfectly fine.
