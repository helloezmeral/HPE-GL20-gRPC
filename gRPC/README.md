# HPE-GL20-gRPC
Version number 1

## File explaination
```sh
├── Client.py
        # This is the Client-side Code 
├── GL20_pb2_grpc.py
        # Generated code from .proto. Required to run on both side
├── GL20_pb2.py
        # Generated code from .proto. Required to run on both side
├── GL20.proto
        # .proto file to define the communication between client and server
├── gRPC_server.py
        # Server-side code which run on GL20
├── pyGL20.py
        # Library to run on top of GL20
└── serviceCode.py
        # A module for translating code from gRPC to local
```
Files requried to run

Server:
- GL20_pb2_grpc.py ,  GL20_pb2.py
- serviceCode.py
- pyGL20.py
- gRPC_server.py

Server:
- GL20_pb2_grpc.py ,  GL20_pb2.py
- Client.py

# Step to develop Microservice
## Step 1: Write the Protocol buf
```
syntax = "proto3";

message GPIO {
    int32 PINx = 1;
    int32 value = 2;
    bool level = 3;
}


service serviceGL20 {
    rpc digitalWriteToggle(GPIO) returns (GPIO) {}
    rpc digitalWriteToggleAll(GPIO) returns (GPIO) {}
    rpc digitalReadAll(GPIO) returns (GPIO) {}
    rpc digitalRead(GPIO) returns (GPIO) {}
    rpc digitalWrite(GPIO) returns (GPIO) {}
    rpc digitalWriteAll(GPIO) returns (GPIO) {}
}

```

## Step 2: Complie the .proto 

```py
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. *.proto
```

## Step 3: Write the serviceCode.py
This serviceCode is for translating the client side calling to local calling

## Step 4: Run the gRPC server
Remember to register to the service and mark the response
```py
sudo python gRPC_server.py
```
Client-side
---
## Step 5: transfer the two pb.py file to the target client

## Step 6: Remote call the function with

```py
    """serviceGL20 Create API for your to control the GPIO of GL20 
    """

    def digitalWriteToggle(self, request, context):
        """Toggle the OUTPUT port specific pin (PIN6, PIN7)
            ex: stub.digitalWriteToggle(GL20_pb2.GPIO(PINx = 6))
        """

    def digitalWriteToggleAll(self, request, context):
        """Toggle the OUTPUT port pins (PIN6, PIN7)
            ex: stub.digitalWriteToggleAll(GL20_pb2.GPIO())
        """

    def digitalReadAll(self, request, context):
        """Read all pin and return in byte form
            ex: bin(stub.digitalReadAll(GL20_pb2.GPIO()).value)
        """

    def digitalRead(self, request, context):
        """Read a specific pin and return True if Logic HIGH
            ex: stub.digitalRead(GL20_pb2.GPIO(PINx = 6)).level
        """

    def digitalWrite(self, request, context):
        """Write a specific pin
            ex: stub.digitalWrite(GL20_pb2.GPIO(PINx = 6, level = True))
        """

    def digitalWriteAll(self, request, context):
        """Assign both PIN6 and PIN7 simultaneously
            ex: stub.digitalWriteAll(GL20_pb2.GPIO(value = 2))
        """
```


```proto3
syntax = "proto3";

message GPIO {
    int32 PINx = 1;  // Logic pin on Gl20
    int32 value = 2; // Value for return the whole port value and value to write the two output port
    bool level = 3; // True represent logic High on GPIO
}

/* serviceGL20 Create API for your to control the GPIO of GL20 */
service serviceGL20 {
    //Toggle the OUTPUT port specific pin (PIN6, PIN7)
    rpc digitalWriteToggle(GPIO) returns (GPIO) {}

    //Toggle the OUTPUT port pins (PIN6, PIN7)
    //      ex: stub.digitalWriteToggleAll(GL20_pb2.GPIO())
    rpc digitalWriteToggleAll(GPIO) returns (GPIO) {}

    /*Read all pin and return in byte form
        
        ex: bin(stub.digitalReadAll(GL20_pb2.GPIO()).value)*/
    rpc digitalReadAll(GPIO) returns (GPIO) {}

    // Read a specific pin and return True if Logic HIGH
    //      ex: stub.digitalRead(GL20_pb2.GPIO(PINx = 6)).level
    rpc digitalRead(GPIO) returns (GPIO) {}

    // Write a specific pin
    //      ex: stub.digitalWrite(GL20_pb2.GPIO(PINx = 6, level = True))
    rpc digitalWrite(GPIO) returns (GPIO) {}

    /* Assign both PIN6 and PIN7 simultaneously
        
        ex: stub.digitalWriteAll(GL20_pb2.GPIO(value = 2))
         */
    rpc digitalWriteAll(GPIO) returns (GPIO) {}
}

// Command
// python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. *.proto
```


