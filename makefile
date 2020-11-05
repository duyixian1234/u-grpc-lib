proto:
	rm -rf u_grpc_lib
	python -m grpc_tools.protoc -I protos --python_out=. --grpc_python_out=. protos/u_grpc_lib/*.proto

build: proto
	rm -rf dist
	poetry build

publish: build
	poetry config pypi-token.repo "${PYPI_TOKEN}"
	poetry publish -r repo