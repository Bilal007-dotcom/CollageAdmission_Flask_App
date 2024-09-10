# CollageAdmission_Flask_App



#Download mysql image 

  
docker pull mysql:5.7

docker images

#Create docker project directory
mkdir docker-project
cd docker-project

#Clone the repository from github
git clone https://github.com/Bilal007-dotcom/two-tier-flask-app.git
ls
cd two-tier-flask-app
ls

#Create image from docker file
docker build -t flask-app:latest   .
docker images

#Create volume
docker volume ls   [check volume]
docker volume create mysql_data  [create data]
docker volume ls
docker volume inspect mysql_data

# Create user-defind Network
Note: For communication between container to container,docker network is required.
Note: One container can connect to another container by their names.
docker network ls
docker network create twotier
docker network ls


# Create container from mysl image and create database

docker run -d --name mysql_demo -v mysql_data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root  mysql:5.7
 
docker ps

Note: Go into container and mysql database and create database [i.e. persist volume ]

docker exec -it mysql_demo bash
mysql -u root -p
Enter password:         [i.e. root]

mysql> show databases;

mysql> create database CollageAdmission;

mysql> show databases;

mysql> use CollageAdmission;

mysql> show tables;

mysql> CREATE TABLE IF NOT EXISTS admission_form (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    dob DATE NOT NULL,
    gender VARCHAR(10) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    address TEXT NOT NULL,
    course VARCHAR(100) NOT NULL
);

mysql> show tables;

mysql> exit
exit

# Stop and remove mysql container

docker stop mysql_demo && docker rm mysql_demo
docker ps -a
docker ps


#Again create container from mysql with volume and Network
docker run -d -v mysql_data:/var/lib/mysql --network twotier --name mysql  -e MYSQL_DATABASE=CollageAdmission  -e MYSQL_ROOT_PASSWORD=root mysql:5.7

# Create container from flask-app
Note: Just have a look on source code to get environment variable
docker run -d --network twotier --name two-tier-app -p 5000:5000 -e MYSQL_HOST=mysql  -e MYSQL_USER=root -e MYSQL_PASSWORD=root -e MYSQL_DB=CollageAdmission  flask-app:latest

# Check on Browser 
 IP:5000 
 
 Note: Add some data on GUI 
 
 # Go into mysql container to check data base table
 
 docker exec -it  mysql /bin/bash
 
 mysql -u root -p 
 
 Enter password :    [i.e. root]
 mysql> show databases;
 mysql> use CollageAdmission;
 
 mysql> show tables;
 mysql> select * from admission_form;
 
 mysql> exit
 exit

# Now see data on volumes
docker volume ls
docker inspect mysql_data 

sudo -i
cd /var/lib/docker/volumes/mysql_data/_data/
ls
cd CollageAdmission
ls
