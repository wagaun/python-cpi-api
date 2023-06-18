from concurrent import futures
import logging

import grpc
import generated.cpi_api_pb2_grpc as cpi_api_pb2_grpc
import services.cpi_api_service


def startServer():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    cpi_api_pb2_grpc.add_CpiApiServicer_to_server(
        services.cpi_api_service.CpiApiService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    startServer()
