-- createing a test db table
create database if not exists hbnb_test_db;

-- to use the db
use hbnb_test_db;

-- creating or using an existing user
create user if not exists 'hbnb_test'@'localhost' identified by 'hbnb_test_pwd';

-- granting all privileges to the user
grant all privileges on hbnb_test_db.* to 'hbnb_test'@'localhost';

-- granting select privileges on perfomance_schema
grant select on perfomance_schema.* to 'hbnb_test'@'localhost';
