import grpc

# import the generated classes
import GL20_pb2
import GL20_pb2_grpc

import time
import timeit

GL20_IP = "127.0.0.1:50051"

# Blinking
def run():
    with grpc.insecure_channel(GL20_IP) as channel:
        stub = GL20_pb2_grpc.serviceGL20Stub(channel)

        myLevel = stub.digitalRead(GL20_pb2.GPIO(PINx = 0)).level
        if myLevel == True:
            stub.digitalWriteToggle(GL20_pb2.GPIO(PINx = 7))
            stub.digitalWrite(GL20_pb2.GPIO(PINx = 6, level = False))
            time.sleep(0.1)
        else:
            stub.digitalWrite(GL20_pb2.GPIO(PINx = 6, level = True))
            stub.digitalWrite(GL20_pb2.GPIO(PINx = 7, level = False))


if __name__ == '__main__':
    while True:
        run()
