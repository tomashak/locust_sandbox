# locust_sandbox
Python framework for performance testing

## Installation
```pip3 install locust```
```pip3 install locust```

## Run tests
Call if you wanna use locust.conf

```locust```

Call without GUI
```locust -f <path_to_file> --no-web -c 50 -r 10```
Hosts: https://jsonplaceholder.typicode.com

### Locust’s web interface
Once you’ve started Locust using one of the above command lines, you should open up a browser and point it to http://127.0.0.1:8089. 


## Example win app (EXE)
https://exiftool.org/
Get Exif information from image files
```exiftool.exe .\example.jpg -json -textout .json```
Output is in file: example.json

## Example web app
We use Prestashop in docker
Detail information: https://github.com/PrestaShop/docker

```
# create a network for containers to communicate
$ docker network create prestashop-net
# launch mysql 5.7 container
$ docker run -ti --name some-mysql --network prestashop-net -e MYSQL_ROOT_PASSWORD=admin -p 3307:3306 -d mysql:5.7
# launch prestashop container
$ docker run -ti --name some-prestashop --network prestashop-net -e DB_SERVER=some-mysql -p 8080:80 -d prestashop/prestashop
```

http://localhost:8085/admin  / nutne odstranit slozku install a prejmenovat slozku admin
tomas.hak@gmail.com  / Abcd1234