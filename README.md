#### Bilding and deploying real-world, fully functional e-commerce application based on Django Made Easy book


### ========
### 1. SETUP
### ========


#### 1.1.1 Setup DONE, refer to README-SETUP.md


### ===============================
### 2 Creating listings application
### ===============================


#### 2.1 Creating listings application

        new file:   .gitignore
        new file:   README-SETUP.md
        new file:   README.md
        new file:   apps/listings/__init__.py
        new file:   apps/listings/admin.py
        new file:   apps/listings/apps.py
        new file:   apps/listings/migrations/__init__.py
        new file:   apps/listings/models.py
        new file:   apps/listings/tests.py
        new file:   apps/listings/urls.py
        new file:   apps/listings/views.py
        new file:   config/__init__.py
        new file:   config/asgi.py
        new file:   config/settings.py
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   manage.py
        new file:   requirements.txt
        new file:   static_in_env/starter.css
        new file:   templates/base.html
        new file:   templates/listings/index.html


#### 2.2 Create and add new database

        modified:   README.md


#### 2.3 Create Category and Product models

        modified:   README.md
        modified:   apps/listings/models.py


#### 2.3 Creating and applying migrations

        modified:   README.md
        new file:   apps/listings/migrations/0001_initial.py


#### 2.4 Creating administration site (create superuser)

        > (venv3932) λ python manage.py createsuperuser

        modified:   README.md


#### 2.5 Adding models to the administration site

        modified:   README.md
        modified:   apps/listings/admin.py
        modified:   apps/listings/models.py


#### 2.6 Customizing how models are displayed

        modified:   README.md
        modified:   apps/listings/admin.py


#### 2.7 Inserting categories and products

        modified:   README.md


#### 2.8 Displaying our categories and products Part 1 - Building our product list view

        modified:   README.md
        modified:   apps/listings/views.py


#### 2.9 Displaying our categories and products Part 2 - Creating template for our product list

        modified:   README.md
        new file:   static_in_env/css/bootstrap.min.css
        new file:   static_in_env/css/fonts/google-fonts.css
        new file:   static_in_env/css/style.css
        new file:   static_in_env/js/scripts.js
        modified:   templates/base.html
        renamed:    templates/listings/index.html -> templates/product/detail.html
        new file:   templates/product/list.html