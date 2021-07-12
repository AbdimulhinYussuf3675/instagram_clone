# Instagram_clone

## Author
### [Abdimulhin Adan](https://github.com/AbdimulhinYussuf3675)
## Description
Instagram_clone is simply a clone of the website for the popular photo app Instagram


## Setup Instructions:
### Requirements

##### 1. Clone the repository
Clone the the repository by running

   ```bash
   git clone https://github.com/AbdimulhinYussuf3675/instagram_clone.git
   ```
 or download a zip file of the project from github


Navigate to the project directory
```bash
cd instagram_clone
```

##### 2. Create a virtual environment
 Install `Virtualenv`

   ```prettier
   python3 -m venv venv
   ```

To create a virtual environment named `virtual`, run

   ```prettier
   python3 -m venv Virtual
   ```
To activate the virtual environment we just created, run

   ```bash
   source virtual/bin/activate
   ```
##### 3. Create a django and create django projects
 Install django
 ```bash
 pip install django==1.11
  ```
  Create django project
  ```bash
  django-admin startproject instagram.
```
create a clone app
 ```bash
 django-admin startapp clone
 ```



##### 5. Create a database
You'll need to create a new postgress database, Type the following command to access postgress
   ```bash
    $ psql
   ```
   Then run the following query to create a new database named ```insta```
   ```
   # create database insta
   ```


#####  4.Install dependencies
To install the requirements from `requirements.txt` file,

   ```prettier
   pip install -r requirements.txt
   ```

#####  5.Create Database migrations
Making migrations on postgres using django

```prettier
python manage.py makemigrations gallery
```


then run the command below;

 ```bash
 python manage.py migrate
 ```

##### 6.Run the app
To run the application on your development machine,

    python3 manage.py runserver

## Technologies Used
* Django
* Python
* Html
* Css
* Bootstrap3
* Django-Admin


## User stories
>As a user I should be able to:

* Sign in to the application to start using.
* Upload my pictures to the application.
* See my profile with all my pictures.
* Follow other users and see their pictures on my timeline.
* Like a picture and leave a comment on it.

## Bugs
* Displaying posts and some functionality of likes and follow

## License
[![License](https://img.shields.io/packagist/l/loopline-systems/closeio-api-wrapper.svg)](http://opensource.org/licenses/MIT)
>MIT license &copy;  2021 Abdimulhin

# Collaboration Information
* Clone the repository
* Make changes and write tests
* Push changes to github
* Create a pull request

# Contacts
adam.abdimulhi.001@gmail.com