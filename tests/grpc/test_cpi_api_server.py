import grpc

from datetime import datetime

import pythoncpiapi.grpc.generated.cpi_api_pb2_grpc as cpi_api_pb2_grpc
import pythoncpiapi.grpc.generated.cpi_api_pb2 as cpi_api_pb2


def testGrpcEndpoint():
    channel = grpc.insecure_channel('localhost:50051')
    stub = cpi_api_pb2_grpc.CpiApiStub(channel)
    request = cpi_api_pb2.GetCpiTimeRequest()
    timeSeries = stub.GetCpiTimeSerie(request)
    assert len(timeSeries.results) == 2
    assert timeSeries.results[0].value == 42.0
    ts = timeSeries.results[0].month
    print(ts)
    dt = datetime(ts.seconds)
    assert dt.day == 1
    # assert dt.month == 4
    assert dt.year == 2023
