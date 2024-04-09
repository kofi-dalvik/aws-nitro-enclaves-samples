docker build -t vsock-sample-server -f Dockerfile .
nitro-cli build-enclave --docker-uri vsock-sample-server --output-file vsock_sample_server.eif
nitro-cli run-enclave --config enclave.json
