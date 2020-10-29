Success Code:
only localhost
sudo docker run -it --device /dev/i2c-0 -p 127.0.0.1:50051:50051 mygl20

Local network ok
sudo docker run -it --device /dev/i2c-0 -p 50051:50051 mygl20
sudo docker run -it --device /dev/i2c-0 -p 0.0.0.0:50051:50051 mygl20

Test Code:
sudo docker run -it --device /dev/i2c-0 --expose 50051 mygl20
sudo docker run -it --device /dev/i2c-0 -p 50051:50051 mygl20