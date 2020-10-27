# HPE-GL20-gRPC
(Under Development)

GitClone the project

# Step 1: Write the Protocol buf


# Step 2: Complie the .proto 

```py
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. GL20.proto
```

# Step 3: Write the serviceCode.py
This serviceCode is used to contained all the function which is callable on the client side

# Step 4: Run the gRPC server

# Step 5: transfer the two pb.py file to the target client

# Step 6: Remote call the function with

```py
stub.GL20_digitalWriteToggleAll(GL20_pb2.noMessage())
```



