# clubsite

A WIP club/announcements backend for schools.

Made using Django 2.1.3.

Main contributor(s): 

* [Jonathan Sumabat](https://github.com/jsumabat)

## Installed Applications

You will need [sortedm2m](https://github.com/gregmuellegger/django-sortedm2m) in order for some pages to work properly. 

## Installing

**General Installation**

I recommend to delete the migrations and reset them through the following steps:

0. Clone the Repository (duh)
1. Delete everything in the `club_management/migrations` folder with the exception of `__init.py__`.
2. Run `python manage.py makemigrations`
3. Run `python manage.py migrate`
4. The application should run perfectly fine.

**Beginner-Friendly Installation**

1. Open up Command Prompt (or Bash)
2. Run the command `py -m pip install django`
3. Run the command `py -m pip install django-sortedm2m`
4. Go to your directory of choice (for storing the program) and run `Git Bash` in that directory
5. In Git Bash, run the command `git clone https://github.com/jsumabat/tssclubsite.git`
6. Go into the directory that the `git clone` command created
7. Run the command `py manage.py makemigrations`
8. Run the command `py manage.py migrate`
9. You're done!

Now, to start the server all you have to do is run the command `py manage.py runserver` in the directory of the program.  If you want to look at what settings you can run the program with, run the command `py manage.py runserver --help`
