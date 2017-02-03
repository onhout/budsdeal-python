# Budsdeal

This project uses Django as backend and React as front end.

## Prerequisite

- Python, Django
- Node, NPM

## How to Install

To start coding this project, follow these steps:

1. [Install Python 3 (OSX)](http://docs.python-guide.org/en/latest/starting/install3/osx/#install3-osx)
2. Install Django 

`$ pip install django`

3. Install VirtualEnv 

`$ pip install virtualenv`

4. While inside the project, install the environment

`$ virtualenv env`

5. Activate the environment

`$ source env/bin/activate`

6. Install the requirements, this will install all the needed packages

`$ pip install -r requirements.txt`

If you encountered the error when installing psycopg2, [Click here](http://stackoverflow.com/questions/28253681/you-need-to-install-postgresql-server-dev-x-y-for-building-a-server-side-extensi)

7. [Install Node.js](https://nodejs.org/en/download/)
8. Install gulp-cli globally

`$ npm install gulp-cli -g`

9. While inside the project, install the npm packages

`$ npm install`

10. Start the project, one is to host the server using Python
`$ python manage.py runserver`
then fire up another terminal and run 
`$ gulp` to watch JavaScript changes

## Merging your code

1. Fork my shit, then:
    
    
    $ git clone https://github.com/YOURGITHUB/budsdeal-python.git
    
2. Make your changes, then:


    $ git add .
    $ git commit -m "Commit message"
    $ git push origin master
    
    
3. Go to the forked repository and send a pull request by clicking "new pull request"~ Explain your shit.
4. Then I'll do my part and merge it lol.

As always, [Google](http://www.google.com) is your best friend.