# Geolocation 
## :information_source: Information 


The project aims to search for locations according to the characteristics and city typed by the user, such as: "Restaurant" and "New York". The YELP API was used to perform the data search, for more information on using the API go to: https://www.yelp.com/developers/documentation/v3.
A map has been placed for the user to better locate the location using openstreet to display the map. For the addresses searched, the GEOIP2 database was used. For more information on using GEOIP2, go to: https://dev.maxmind.com/geoip.

## ⚠️ Prerequisite

![](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)

![](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

![](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)

![](https://img.shields.io/badge/MySQL-00000F?style=for-the-badge&logo=mysql&logoColor=white)

## Demo


## ⚙️ Creating virtual machine

Create your virtual machine
```
python3 -m venv venv
```
Activate your virtual machine
```
source venv/bin/activate
```
After the virtual machine is activated, install the project dependencies
```
pip install -r requirements.txt```
```

## ⚙️ Installing MySQL

Enter the following commands in the terminal.

```
sudo apt update
sudo apt install mysql-server

```
### Configuring MySQL

For new installations, you will want to run the security script that is included. This changes some of the less secure default options for things like root logins and example users. Enter the command below.

```
sudo mysql_secure_installation
```
This will take you through a series of prompts where you can make some changes to the security options of your MySQL installation. The first prompt will ask you if you want to configure the Validate Password Plugin, which can be used to test the strength of your MySQL password. Regardless of your choice, the next prompt will be to set the password for the MySQL root user. Sign in and then confirm a secure password of your choice.

From there, you can press Y and then ENTER to accept the default answers for all subsequent questions. This will remove some anonymous users and the test database, disable remote login for root, and load all of these new rules so that MySQL immediately respects the changes you made.

### Testing MySQL

To see if MYSQL is running, type the following command.

```
systemctl status mysql.service
```

If MySQL is not running, you can start it with the following command.
```
sudo systemctl start mysql
```
Now try to connect your root user to MySQL.
```
mysql -u root -p
```
## :rocket: Installation

![](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)

```sh
git clone https://github.com/RamonBecker/AppGeolocation.git
```

![](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)


```sh
git clone https://github.com/RamonBecker/AppGeolocation.git
or install github https://desktop.github.com/ 

```

## :zap: Technologies	

- Python
- GEOLite2
- OpenStreet




## :memo: Developed features

- [x] Search for the term (characteristic) of the location;
- [x] Search by the specific city of a location;
- [x] In the search performed, the map of the locations is shown.


## :technologist:	 Author

By Ramon Becker 👋🏽 Get in touch!



[<img src='https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/github.svg' alt='github' height='40'>](https://github.com/RamonBecker)  [<img src='https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/linkedin.svg' alt='linkedin' height='40'>](https://www.linkedin.com/in/https://www.linkedin.com/in/ramon-becker-da-silva-96b81b141//)
![Gmail Badge](https://img.shields.io/badge/-ramonbecker68@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:ramonbecker68@gmail.com)



