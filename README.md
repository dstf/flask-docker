## Template for Installing and deploying a simple API App starter with Flask + Gunicorn + Nginx + SSL self-signed + Mongodb inside a Docker container. (Debian 10)



## Installation

- Clone the repository
```
git clone https://github.com/dstf/flask-docker.git
```

- Change the $domain inside the file named:
```
./nginx./app.conf
```
  and the root password for your database inside:
```
./docker-compose.yml and ./app/app.py
```

- Run the script installing (Docker & Docker compose)
```
sh install-docker.sh
```

- Run the enviroment
```
sh enviroment.sh
```



![](https://06a7f2c2-5c56-40d7-aded-6455af08391b.es-mad1.upcloudobjects.com/project001/github/simpleAPI.gif)


## Self-SSL method:
```
curl --insecure -i https:// 
```

## Curl example 
GET
```
curl  -i https://api.fixerupper.me/
```
POST
```
curl  -i -H "Content-Type: application/json" -X POST -d '{"username":"dstf", "message": "hello word"}' https://api.fixerupper.me/v1 
```
DELETE
```
curl -i -H "Content-Type: application/json" -X DELETE -d '{"username":"dstf", "message": "hello word"}' https://api.fixerupper.me/v1
```

