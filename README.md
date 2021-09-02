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


#### 2.10 Displaying our categories and products Part 3 - Views and urls for produc list

        modified:   apps/listings/urls.py
        modified:   apps/listings/views.py
        new file:   static_in_env/css/admin.css
        new file:   static_in_env/css/pdf.css        


#### 2.11 Displaying our categories and products Part 4 -  Filtering by category

        modified:   README.md
        modified:   apps/listings/models.py
        modified:   apps/listings/urls.py
        modified:   apps/listings/views.py
        modified:   templates/product/list.html


#### 2.12 Product detail page

        modified:   README.md
        modified:   apps/listings/models.py
        modified:   apps/listings/urls.py
        modified:   apps/listings/views.py
        modified:   templates/product/detail.html
        modified:   templates/product/list.html


#### 2.13 Review - Adding reviews modal

        modified:   README.md
        modified:   templates/product/detail.html


#### 2.14 Review - Create Review model and apply migrations

        modified:   README.md
        new file:   apps/listings/migrations/0002_auto_20210902_0712.py
        modified:   apps/listings/models.py


#### 2.15 Review - Create Review form

        modified:   README.md
        new file:   apps/listings/forms.py


#### 2.16 Review - Adding conditional to views and modified textarea detail page

        modified:   README.md
        modified:   apps/listings/views.py
        modified:   templates/product/detail.html


#### 2.17 Review - Modified label rating html attributes using django form attributes
        
        modified:   README.md
        modified:   templates/product/detail.html


#### 2.18 Review - Re-modified 2.17 

        modified:   README.md
        modified:   templates/product/detail.html


#### 2.19 Review - Re-modified 2.18

        modified:   README.md
        modified:   templates/product/detail.html


#### 2.20 Review - Removing REVIEW_CHOICES rating in forms.py

        modified:   README.md
        modified:   apps/listings/forms.py


#### 2.21 Review - Register Review model to admin

        modified:   README.md
        modified:   apps/listings/admin.py


#### 2.22 Review - Showing review in detail page

        modified:   README.md
        modified:   templates/product/detail.html


#### 2.22 Define get_average_review_score function for average rating calculation for our products

        modified:   README.md
        modified:   apps/listings/models.py

