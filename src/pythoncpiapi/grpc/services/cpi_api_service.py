import generated.cpi_api_pb2 as grpcmodel
import generated.cpi_api_pb2_grpc as grpcapi
from google.protobuf.timestamp_pb2 import Timestamp
from datetime import datetime

class CpiApiService(grpcapi.CpiApiServicer):
    def GetCpiTimeSerie(self, request, context):
        outputDT = datetime(2023, 4, 1)
        outputTS = Timestamp()
        outputTS.seconds = int(outputDT.timestamp())
        response = grpcmodel.GetCpiTimeResponse(results=[
            grpcmodel.Result(month=outputTS, value=42.0)
        ])
        return response
        
