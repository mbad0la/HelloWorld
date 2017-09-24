# HelloWorld
ODIN's Public Platform.

## Contribution Guide
* **Backend**
  All commits are to be made on the _server_ branch.
* **Frontend**
  All commits are to be made on the _client_ branch.

## Installation
```
git clone https://github.com/o-d-i-n/HelloWorld.git && cd HelloWorld
```
```
[sudo] pip install -r requirements.txt
```
```
cd app/client
```
```
[sudo] npm install
```
```
[sudo] npm run build
```
```
cd ../../
```
Create a **config.py** file here with the following contents.
```
MYSQL_USERNAME = 'DB_USER'
MYSQL_PASSWORD = 'DB_PASSWORD'
MYSQL_HOSTNAME = 'localhost'
MYSQL_DATABASE = 'DB_NAME'
```

If you don't have MySQL then run this first.
```
[sudo] apt-get install mysql-server 
```

Adding the MySql database into your system.
```
 mysql -u root -p --execute "create database DB_NAME; grant all on DB_NAME.* to DB_USER@localhost identified by 'DB_PASSWORD';"
``` 

Continue with the following to run the project.
```
python manage.py migrate
```
```
python manage.py setup
```
```
python manage.py runserver
```

## Contributors
All the contributions have been now moved to [Contributors](CONTRIBUTORS.md) file.

This project follows the [all-contributors](https://github.com/kentcdodds/all-contributors) specification.
