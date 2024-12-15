# Introduction
 full stack web application with a framework danago Python.
Bbook store to display, create and publish books, add authors and publishers, display details about each book, and a special page for management. CRUd operations for admin


## Project Structure Project Application
After configuring Django, by deleting its files using cmd, we do the following.

### Step 1: Create a danago project and name it bookstor from the command
```
python manage.py startproject bookstore
```
 ### Step 2: Create an application inside the project and name it bookstorapp and in the settings page
Write the name of the application in INSTALLED_APPS

INSTALLED_APPS = [
'django.contrib.admin',
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.messages',
'django.contrib.staticfiles',
'bookstreapp',
]

### Step 3: Create an env page to add sensitive parameters such as SECRET_KEY
By writing the following command in cmd
```
pip install python-dotenv
```
And copy the SECRET_KEY from the settings page to the env page

### Step 4: Link the project with the postgre database We download postgre We create a superuser We write the commands in cmd
```
python manage.py cratesuperuser 
```
In the settings page, we change the default settings for the database
```
DATABASES = {
"default": {
"ENGINE": "django.db.backends.postgresql",
"NAME": "books",
"USER": "saleem",
"PASSWORD": "11111",

}
}
```
### Step 5: Write links in the urls page of the main project
```
path('',include('bookstreapp.urls')),
```
And create a urls page for the application The main link in the urls in the main project takes us to the links of the urls page of the application

Special step: In the models page, we write three classes between class books and class Author A one-to-one relationship through ForeignKey
To create application tables and add the required elements in the tables, write the following commands in cmd
```
python manage.py makemigration

python manage.py migration
```

### Step 6: Write the functions in the application work in the views.py page
A function, URL and dashboard page were built to manage the delete, add and update operations (crud).

### Step 7: Create a folder named templates and create html pages to display the project. Write the display pages in a folder and include bootstarp

To run the project and display it on the server, write the following command
```
python manage.py runserver
```
