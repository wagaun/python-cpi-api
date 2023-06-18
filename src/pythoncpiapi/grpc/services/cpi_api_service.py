from google.protobuf.timestamp_pb2 import Timestamp
from datetime import datetime
from services.repo.cpi_series_repository import find_cpi_data

import generated.cpi_api_pb2 as grpcmodel
import generated.cpi_api_pb2_grpc as grpcapi


def fromDateTimeToTimestamp(date: datetime) -> Timestamp:
    outputTS = Timestamp()
    outputTS.seconds = int(date.timestamp())
    return outputTS


class CpiApiService(grpcapi.CpiApiServicer):
    def GetCpiTimeSerie(self, request, context):
        response = grpcmodel.GetCpiTimeResponse(
            results=[grpcmodel.Result(
                month=fromDateTimeToTimestamp(cpiData.date),
                value=cpiData.value)
                for cpiData in find_cpi_data()
            ])
        return response
