# python-cpi-api
API Made to learn python

## Setup
Follow instructions from [here](https://python-poetry.org/docs/) to setup Poetry.

## Development
There are a few steps that are important to start development:

- Start poetry virtualenv
``poetry shell``

- Install dependencies
``poetry install --no-root``

- How to compile the proto files
``python3 -m grpc_tools.protoc -Iprotos --python_out=src/pythoncpiapi/grpc/generated --pyi_out=src/pythoncpiapi/grpc/generated --grpc_python_out=src/pythoncpiapi/grpc/generated protos/cpi-api.proto``

- Flake
``flake8``

- Run the service
``python3 src/pythoncpiapi/grpc/cpi_api_server.py``

- Run tests (it must be executed with the service running for now)
``pytest``

- grpcurl command for testing
``grpcurl -plaintext localhost:50051 cpiapi.CpiApi/GetCpiTimeSerie``

- start docker containers
``docker-compose up``

# Known issues/next steps
- protoc generated files are not working properly.
- grpcurl command doesn't work
- contenariaze the service
