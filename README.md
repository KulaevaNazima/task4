# Courses

A Rest API project with using Django Rest Framework to view, create and delete courses. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

## Prerequisites

This project is written using Python, Django and Django Rest Framework.

 

1.  Create a project folder 

    ```

    $ mkdir 'project_folder_name'

    ```

    and go to folder with command 

 

    ```

    $ cd 'project_folder_name'

    ```

2.  Clone the project 

    ```

    $ git clone https://github.com/KulaevaNazima/task4.git

    ```

3.  Create the virtual environment 

    ```

    $ python3 -m venv venv

 

    $ source venv/bin/activate

    ```

4.  Install the requirments

    ```

    $ pip install -r requirements.txt

    ```

5. Make migrations

    ```

    $ python manage.py makemigrations

 

    $ python manage.py migrate

    ```

6. Create a superuser

    ```

    $ python manage.py createsuperuser

    ```

7. Now, we can start the server

    ```

    $ python3 manage.py runserver

    ```

## Created with

 

- Django - framework for web applications

- Django REST Framework - toolkit for building Web APIs

##  API Docementation
Go to [https://app.apiary.io/courses32/editor](https://app.apiary.io/courses32/editor)
