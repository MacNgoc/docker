#Pull image from hub.docker (version latest)
docker pull mysql

# Environment Variable
#port : 3306

# root: MYSQL_ROOT_PASSWORD

# MYSQL_DATABASE, MYSQL_USER, MYSQL_PASSWORD

# Configuration file
/etc/mysql/my.cnf
    * add: default-authentication-plugin=mysql_native_password

# where is database 
/var/lib/mysql

# run mysql container with share data 
docker run --name some-mysql -v /my/own/datadir:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mysql:tag

# run mysql container with terminal
docker run -it --network some-network --rm mysql mysql -hsome-mysql -uexample-user -p

# container shell access and viewing MySQL logs
docker exec -it some-mysql bash

docker logs some-mysql



########################### HOW TO RUN ########################

1) Run a mysql container to extract file configuration my.cnf
docker run --rm -v /Users/bnmac/Documents/Travail/docker/mysql/:/home/mycode mysql cp /etc/mysql/my.cnf /home/mycode/

2) Add "default-authentication-plugin=mysql_native_password" to configuration's file my.cnf

3) mkdir "db" --> save database in case deletion of container

4) docker run -e MYSQL_ROOT_PASSWORD=abc123 -v /Users/bnmac/Documents/Travail/docker/mysql/my.cnf:/etc/mysql/my.cnf -v /Users/bnmac/Documents/Travail/docker/mysql/db:/var/lib/mysql --name my-mysql mysql

5) Enter the container 
docker exec -it my-mysql bash

6) Test mysql
mysql -u root -pabc123

7) Some sql querry
show databases;
CREATE USER 'testuser'@'%' IDENTIFIED BY 'testpass';

#Create database
create database db_testdb;

#Cấp quyền cho user testuser trên db - db_testdb
GRANT ALL PRIVILEGES ON db_testdb.* TO 'testuser'@'%';
flush privileges;

show database;           

exit;                     
