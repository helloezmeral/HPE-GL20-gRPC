import grpc

# import the generated classes
import GL20_pb2
import GL20_pb2_grpc

import time

GL20_IP = "localhost:50051"

# Blinking
def run():
    with grpc.insecure_channel(GL20_IP) as channel:
        # from channel initiate a stub
        stub = GL20_pb2_grpc.serviceGL20Stub(channel)

        # shows some example of calling gRPC, check GL20.proto file
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
