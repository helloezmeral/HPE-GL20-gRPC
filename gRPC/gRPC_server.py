import grpc
from concurrent import futures
import time
import logging

# import the generated classes
import GL20_pb2
import GL20_pb2_grpc

# import the original calculator.py
import serviceCode

class serviceGL20(GL20_pb2_grpc.serviceGL20Servicer):

    def digitalWriteToggle(self, request, context):
        response = GL20_pb2.GPIO()
        print(request.PINx)
        serviceCode.digitalWriteToggle(request.PINx)
        return response
    
    def digitalWriteToggleAll(self, request, context):
        response = GL20_pb2.GPIO()
        serviceCode.digitalWriteToggleAll()
        return response

    def digitalReadAll(self, request, context):
        response = GL20_pb2.GPIO()
        response.value = serviceCode.digitalReadAll()
        return response

    def digitalRead(self, request, context):
        response = GL20_pb2.GPIO()
        response.level = serviceCode.digitalRead(request.PINx)
        return response

    def digitalWriteAll(self, request, context):
        response = GL20_pb2.GPIO()
        serviceCode.digitalWriteAll(request.value)
        return response

    def digitalWrite(self, request, context):
        response = GL20_pb2.GPIO()
        serviceCode.digitalWrite(request.PINx, request.level)
        return response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    GL20_pb2_grpc.add_serviceGL20Servicer_to_server(serviceGL20(), server)
    print('Starting server. Listening on port 50051.')
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()