# Description
#### Small chat template app based on pure django (with django authentication) and ajax client page. Client page uses jQuery.

# Local setup in debial/ubuntu
`git clone https://github.com/AcckiyGerman/django-simple-chat-app/`  
`cd django-simple-chat-app`  

### create virtual environment
#### either by python utility (sudo apt install python3-venv):
`python3 -m venv venv`  
#### or you can use virtualenv (sudo apt install virtualenv):
`virtualenv venv`  

### load environment
`source venv/bin/activate`  

### initialize project
`pip install -r requirements.txt`  
`python manage.py makemigrations chatroom`  
`python manage.py migrate`  
`python manage.py createsuperuser`  

### run
`python manage.py runserver`  

#### Now go to http://localhost:8000 and check the site is working (login page must to appear)
#### then go to http://localhost:8000/admin , log in with admin credentials and in the Django admin page you can create few users to test the chat.

#### Use chat itself on http://localhost:8000/
