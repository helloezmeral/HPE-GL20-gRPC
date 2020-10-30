# This is the docker Command you need to run
only localhost
```sh
sudo docker run -it --device /dev/i2c-0 -p 127.0.0.1:50051:50051 mygl20
```
Local network ok
```sh
sudo docker run -it --device /dev/i2c-0 -p 50051:50051 mygl20
sudo docker run -it --device /dev/i2c-0 -p 0.0.0.0:50051:50051 mygl20
sudo docker run -it --device /dev/i2c-0 -p 50051:50051 helloezmeral/gl20ms:latest
```

- Note that the device may change (if the device change and you need to rebuild to image again)
