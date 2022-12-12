# 說明
1. 使用docker-compose建立flask app部署環境
2. --scale app=3, 可開三個service
3. 利用nginx讓瀏覽器引導到其中一個service, 得到負載平衡(load balancing)效果

### Run docker-compose
```
docker-compose up -d --build --scale app=3
```