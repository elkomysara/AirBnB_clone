-- create or use a database
create database if not exists hbnb_dev_db;

-- to use the database
create user if not exists 'hbnb_dev'@'localhost' identified by 'hbnb_dev_pwd';

-- granting all provileges to hbnb_dev on hbnb_dev_db
grant all privilegeson hbnb_dev_db.* to 'hbnb_dev'@'localhost';
