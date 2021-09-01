# MEMBUAT APLIKASI ECOMMERCE YG BERFUNGSI SCR PENUH MENGGUNAKAN DJANGO V3.2

https://github.com/gurnitha/django_ecommerce_venam


### ================
### 	1. SETUP
### ================


#### 1.1.1 Initial commit - Membuat local repository

        E:\workspace\django-ecommece\django_ecommerce_venam
        λ touch .gitignore README.md
        λ git init
        λ git add .
        λ git status
        λ git add .
        λ git commit -m "1.1.1 Initial commit - Membuat local repository"

        new file:   .gitignore
        new file:   README.md


#### 1.2.2 Membuat remote repository di Gihub

        https://github.com/gurnitha/django_ecommerce_venam

        modified:   README.md


#### 1.3.3 Membuat virtual environment

        modified:   .gitignore
        modified:   README.md


#### 1.4.4 Menginstal Django

        modified:   README.md 


#### 1.5.5 Meng-upgrade pip

        modified:   README.md



### =================================
### 	2. DJANGO PROJECT DAN APP
### =================================


#### 2.1.6 Membuat Django project dgn nama 'config'

        modified:   README.md
        new file:   config/__init__.py
        new file:   config/asgi.py
        new file:   config/settings.py
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   manage.py


#### 2.2.7 Membuat Django dgn nama 'apps/main'

        modified:   README.md
        new file:   apps/main/__init__.py
        new file:   apps/main/admin.py
        new file:   apps/main/apps.py
        new file:   apps/main/migrations/__init__.py
        new file:   apps/main/models.py
        new file:   apps/main/tests.py
        new file:   apps/main/views.py
        new file:   config/__pycache__/__init__.cpython-39.pyc
        new file:   config/__pycache__/settings.cpython-39.pyc


#### 2.3.8 Meregistrasi main app pada django project 'settings.py'

        modified:   README.md
        modified:   apps/main/apps.py
        modified:   config/settings.py


#### 2.4.9 Menjalankan server

        modified:   README.md
        new file:   apps/main/__pycache__/__init__.cpython-39.pyc
        new file:   apps/main/__pycache__/admin.cpython-39.pyc
        new file:   apps/main/__pycache__/apps.cpython-39.pyc
        new file:   apps/main/__pycache__/models.cpython-39.pyc
        new file:   apps/main/migrations/__pycache__/__init__.cpython-39.pyc
        modified:   config/__pycache__/settings.cpython-39.pyc
        new file:   config/__pycache__/urls.cpython-39.pyc
        new file:   config/__pycache__/wsgi.cpython-39.pyc
        new file:   db.sqlite3 
 

#### 2.5.9 Structure project 

        .
        ├── README.md
        ├── apps
        │   └── main
        │       ├── __init__.py
        │       ├── __pycache__
        │       ├── admin.py
        │       ├── apps.py
        │       ├── migrations
        │       ├── models.py
        │       ├── tests.py
        │       └── views.py
        ├── config
        │   ├── __init__.py
        │   ├── __pycache__
        │   │   ├── __init__.cpython-39.pyc
        │   │   ├── settings.cpython-39.pyc
        │   │   ├── urls.cpython-39.pyc
        │   │   └── wsgi.cpython-39.pyc
        │   ├── asgi.py
        │   ├── settings.py
        │   ├── urls.py
        │   └── wsgi.py
        ├── db.sqlite3
        ├── manage.py
        └── venv3932
            ├── Include
            ├── Lib
            │   └── site-packages
            ├── Scripts
            │   ├── Activate.ps1
            │   ├── __pycache__
            │   ├── activate
            │   ├── activate.bat
            │   ├── deactivate.bat
            │   ├── django-admin.exe
            │   ├── django-admin.py
            │   ├── pip.exe
            │   ├── pip3.9.exe
            │   ├── pip3.exe
            │   ├── python.exe
            │   ├── pythonw.exe
            │   └── sqlformat.exe
            └── pyvenv.cfg


#### 2.6.10 Menempatkan files project pada Gihub

        modified:   README.md 



### ===================
###     3. DATABASE
### ===================


#### 3.1.11 Instal django environ

        source: https://django-environ.readthedocs.io/en/latest/
        (venv3932) λ pip install django-environ

        modified:   README.md


#### 3.2.12 Install PostgreSQL driver

        (venv3932) λ python -m pip install psycopg2-binary==2.8.6

        modified:   README.md


#### 3.3.13 Create .env file and setup environ

        modified:   .gitignore
        modified:   README.md
        new file:   config/.env


#### 3.4.14 Moving Project's SECRET_KEY to .env file

        modified:   README.md
        modified:   config/.env
        modified:   config/settings.py


#### 3.5.15 Create PostgreSQL database 

        hp=# CREATE DATABASE django_ecommerce_venama;
        CREATE DATABASE
        hp=# 


#### 3.6.16 Menambahkan database kredensial pada .env file

        modified:   README.md
        modified:   config/.env


#### 3.7.17 Konek .env file dengan the project 'settings.py'

        modified:   README.md
        modified:   config/__pycache__/settings.cpython-39.pyc
        modified:   config/settings.py 


#### 3.8.18 Fixing error

        FATAL:  database "django_ecommerce_venam" does not exist

        # drop database
        hp=# drop database django_ecommerce_venama;
        DROP DATABASE

        # create database
        hp=# create database django_ecommerce_venam;
        CREATE DATABASE
        hp=#

        modified:   README.md


#### 3.9.19 Jalankan server untuk menguji koneksi

        (venv3932) λ python manage.py runserver
        ...
        System check identified no issues (0 silenced).
        ...
        Starting development server at http://127.0.0.1:8000/

        modified:   README.md

        NOTE: error fixed
        :)



### =================================
###     4. STATIC DAN MEDIA FILES
### =================================


#### 4.1.20 Setting up static dan media files pada 'settings.py' file

        modified:   README.md
        modified:   config/__pycache__/settings.cpython-39.pyc
        modified:   config/__pycache__/urls.cpython-39.pyc
        modified:   config/settings.py


#### 4.2.21 Membuat path untuk STATIC_ROOT dan MEDIA_ROOT pada 'config/urls.py'

        (venv3932) λ python manage.py check
        System check identified no issues (0 silenced).

        modified:   README.md
        modified:   config/urls.py



### =================================
###     5. REQUIREMENTS.TXT FILE
### =================================


#### 5.1.22 Membuat requirements.txt file

        modified:   README.md
        new file:   requirements.txt


#### 5.2.23 Menulis informasi project ke dalam requirements.txt file

        (venv3932) λ pip freeze > requirements.txt 

        modified:   README.md
        modified:   requirements.txt


### ========================
###     6. MODIFICATION
### ========================


#### Modified to start with HELLO WORLD!





















































































































