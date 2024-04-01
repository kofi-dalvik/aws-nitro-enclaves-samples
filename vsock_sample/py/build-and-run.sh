docker build -t vsock-sample-server -f Dockerfile.server .
nitro-cli build-enclave --docker-uri vsock-sample-server --output-file vsock_sample_server.eif
nitro-cli run-enclave --eif-path vsock_sample_server.eif --cpu-count 2 --memory 256 --debug-mode
