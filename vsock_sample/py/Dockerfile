# Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

FROM python:3.7.9-alpine3.12

COPY vsock.py .

COPY server.py .

CMD ["/usr/local/bin/python3", "server.py"]
