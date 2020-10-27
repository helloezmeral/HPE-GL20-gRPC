import grpc

# import the generated classes
import GL20_pb2
import GL20_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('172.16.11.48:50051')

# create a stub (client)
stub = GL20_pb2_grpc.serviceGL20Stub(channel)


# make the call
stub.GL20_digitalWriteToggleAll(GL20_pb2.noMessage())