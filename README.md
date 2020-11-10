# Locust sandbox


## [Locust.io](https://locust.io/) | [Tesena](https://www.tesena.com/)


## Basic Info
Python framework for performance testing in [Locust.io](https://locust.io/).

## Folder structure
```
Locust_sandbox
└── csv_example                 # Folder with csv file for test
│    └── mysql.csv              # Data for connect to mysql
│    └── test_variables.csv     # Data for tests
└── exif_example                # Folder with exe
│    └── exiftool.exe           # Exe tool
└── locustfiles                 # Folder with test
│    └── csvLibrary             # Script for reading csv
│    └── webpage.py             # File with test
└── locust.conf                 # File for starts locust
└── README.MD                   # Here you are :-)
└── docker-compose.yml          # For more easy starts
```

## Install
- Make sure you have [Docker](https://www.docker.com/) and locust:
    ```pip3 install locust``` 

- If you want to use docker-compose:
    - Go to locust_sandbox folder with cd ```<path_to_repository>```
    - Start docker with ```docker-compose up -d```
    - Go to localhost in your browser and install presta shop
    - Start locust ```locust```

- If you want use docker command:
    - Go to locust_sandbox folder with cd ```<path_to_repository>```
    - Start docker with
        ```
        # create a network for containers to communicate
        $ docker network create prestashop-net
        # launch mysql 5.7 container
        $ docker run -ti --name some-mysql --network prestashop-net -e MYSQL_ROOT_PASSWORD=admin -p 3307:3306 -d mysql:5.7
        # launch prestashop container
        $ docker run -ti --name some-prestashop --network prestashop-net -e DB_SERVER=some-mysql -p 8080:80 -d prestashop/prestashop
        ```
    - Go to localhost in your browser and install presta shop
    - Change name admin directory and delete install folder with FTP or docker CLI 
    - Start locust ```locust```

## Example win app (EXE)
https://exiftool.org/
Get Exif information from image files
```exiftool.exe .\example.jpg -json -textout .json```
