import grpc
from concurrent import futures
import time

# import the generated classes
import GL20_pb2
import GL20_pb2_grpc

# import the original calculator.py
import serviceCode

# create a class to define the server functions
# derived from calculator_pb2_grpc.CalculatorServicer
class serviceGL20Servicer(GL20_pb2_grpc.serviceGL20Servicer):

    # calculator.square_root is exposed here
    # the request and response are of the data types
    # generated as calculator_pb2.Number
    def SquareRoot(self, request, context):
        response = GL20_pb2.Number()
        response.value = serviceCode.square_root(request.value)
        return response

    def GL20_digitalWriteToggleAll(self, request, context):
        response = GL20_pb2.noMessage()
        serviceCode.GL20_digitalWriteToggleAll()
        return response


# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function `add_CalculatorServicer_to_server`
# to add the defined class to the created server
GL20_pb2_grpc.add_serviceGL20Servicer_to_server(
        serviceGL20Servicer(), server)

# listen on port 50051
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)