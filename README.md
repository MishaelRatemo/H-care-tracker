# H.care Tracker

# authors
Mishael Ratemo, Jane Njoroge, Derick ogendi And Alexander Mureithi
# Project descriotion
An application that allows hospitals and clinics to put up a list of their inventory including supplies and medication and allow this information to be plotted on a map.
# Live [Demo](https://hcaretrackers.herokuapp.com/)

# User Stories
**DONOR**
* Create a dispatch order based on a request
* Track the dispatch from manufacturer to client on location and agent.
* Match the submitted inventory with the original dispatch


**Hospital**
* Create a request for supplies
* Request should include specific quantities of specific items
* Receive and update the inventory based on what was received


## Technologies used
    * BackEnd: * Python - Django
    * FontEnd:  jinja2 , CSS,   Bootstrap
    * Database * PostgreSQL * POSTGIS, *GDAL, *PROJ4
    * Leaflet
    * Deployment * Heroku

## Installation / Setup instruction

## Cloning
* Open Terminal {Ctrl+Alt+T}


 git clone ``https://github.com/MishaelRatemo/H-care-tracker``

* cd instagram_clone_django

* Vs code . or atom . based on the text editor you have.

### The application requires the following installations to operate 
* python3
* Postgresql
* Postgis
* Leaflets
* virtual environment - see more on how to install virtual on google
* heroku for online deployment.

#### Requirements
        * asgiref==3.5.0
        * backports.zoneinfo==0.2.1
        * beautifulsoup4==4.10.0
        * certifi==2021.10.8
        * cloudinary==1.29.0
        * confusable-homoglyphs==3.2.0
        * dj-database-url==0.5.0
        * Django==4.0.3
        * django-bootstrap-v5==1.0.11
        * django-cors-headers==3.11.0
        * django-heroku==0.3.1
        * django-leaflet==0.28.2
        * django-registration==3.2
        * djangorestframework==3.13.1
        * fontawesomefree==6.1.1
        * gunicorn==20.1.0
        * psycopg2==2.9.3
        * python-decouple==3.6
        * pytz==2022.1
        * six==1.16.0
        * soupsieve==2.3.1
        * sqlparse==0.4.2
        * urllib3==1.26.9
        * whitenoise==6.0.0
        * -e git+https://github.com/makinacorpus/django-leaflet.git@bb235e1cb3d9e449cf38f58b75dd6e98082eb799#egg=django_leaflet


### Running the application
Once in the cloned folder run the following commands:-
 * #### create Django environnent
        $  python3 -m venv pip virtual -- creates the virtual for runnning your app      
        $ source virtual/bin/env  -- activate  the virtual
        $ pip install -r requirements.txt - this installs all dependecies necessary for app to run
* #### Setup Configurations and Databases
        $ make makemig 
        $ make migrate
* #### Create superuser for the application
        $ make super

* #### Running the application
        $ make run

* #### Running the application
        $ make test

* #### Browse app
        $ 127.0.0.1:8000

## Known Bugs
* There are no known bugs currently but pull requests are allowed incase you spot a bug
* also incase you run it a bug feel free to add or contact

## Contact Information 

If you have any question or contributions and support, please email us at [ratemomishael@gmail.com](ratemomishael@gmail.com)

LinkedIn - [Mishael Ratemo](www.linkedin.com/in/mishael-mosoti-37b786161/)


Portfolio- [Mishael](https://mishaelratemo.github.io/my_portfolio/)
# Licence

Click to  [MIT License](Licence) view

 Copyright (c) 2022 | Mishael Ratemo
