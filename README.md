# Template for Installing and deploying a simple API app with Flask + Gunicorn + Nginx + SSL self-signed + Mongodb inside a Docker container.



## Installation

```
```







![](https://06a7f2c2-5c56-40d7-aded-6455af08391b.es-mad1.upcloudobjects.com/project001/github/simpleAPI.gif)


## Curl example 
```
curl  -i https://api.fixerupper.me/
```
```
curl  -i -H "Content-Type: application/json" -X POST -d '{"username":"dstf", "message": "hello word"}' https://api.fixerupper.me/v1 
```
```
curl -i -H "Content-Type: application/json" -X DELETE -d '{"username":"dstf", "message": "hello word"}' https://api.fixerupper.me/v1
```
Sel-SSL method:
```
curl --insecure -i https:// 
```
