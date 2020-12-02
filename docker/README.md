# Docker Deployment on GL20 gRPC GPIO
# Option 1: Deploy using Docker compose (Recommend)
## Step 1: download the docker compose file
```sh
wget https://github.com/helloezmeral/HPE-GL20-gRPC/releases/download/v0.9/docker-compose.yaml
```
## Step 2: docker-compose up!!!!!
```sh
docker-compose up # run the docker
docker-compose up -d # run the docker in detach model
docker-compose down # shutdown the docker
```
```sh
# or you choose to run online image
sudo docker run -it --device /dev/i2c-0 -p 50051:50051 helloezmeral/gl20ms:latest
```

# Option 2: Build and run your Docker image from scratch
## Step 1: Git Clone all file required
```sh
git clone https://github.com/helloezmeral/HPE-GL20-gRPC
cd HPE-GL-gRPC/docker
```
## Step 2: Customize your Dockerfile
Build your docker image with tag "mygl20"
```sh
sudo docker build . -t mygl20
```

## Step 3: Run your docker
```bash
sudo docker run -it --device /dev/i2c-0 -p 50051:50051 mygl20
sudo docker run -it --device /dev/i2c-0 -p 0.0.0.0:50051:50051 mygl20
```
- Currently the bus is hard code in pyGL20.py
- if the device is not i2c-0, you need to rebuild to image replacing your bus configuration in gRPC_server.py
- You may need to update the gRPC file. [Tutorial](https://github.com/helloezmeral/HPE-GL20-gRPC/tree/main/gRPC)

# Calling Service via gRPC over the network (Client calling)
## STEP 1: Prepare gRPC files
Prepare two files: GL20_pb2_grpc.py, GL20_pb2.py

## STEP 2: Setup environment
```bash
sudo python -m pip install grpcio
```
## STEP 2: Write the Client Code
```py
import grpc

# import the generated classes
import GL20_pb2
import GL20_pb2_grpc

import time

GL20_IP = "localhost:50051"

# Blinking
def run():
    with grpc.insecure_channel(GL20_IP) as channel:
        stub = GL20_pb2_grpc.serviceGL20Stub(channel)
        stub.digitalWriteToggleAll(GL20_pb2.GPIO())
        print(stub.digitalRead(GL20_pb2.GPIO(PINx = 6)).level)
        time.sleep(1)
        print(bin(stub.digitalReadAll(GL20_pb2.GPIO()).value))
        stub.digitalWrite(GL20_pb2.GPIO(PINx = 6, level = True))
        time.sleep(1)
        print(stub.digitalRead(GL20_pb2.GPIO(PINx = 6)).level)
        stub.digitalWriteAll(GL20_pb2.GPIO(value = 2))
        time.sleep(1)


if __name__ == '__main__':
    run()
```
[Document](https://github.com/helloezmeral/HPE-GL20-gRPC/tree/main/gRPC)
