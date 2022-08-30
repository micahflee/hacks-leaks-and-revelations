#!/bin/bash
docker run -it --rm --privileged --pid=host alpine:edge \
    nsenter -t 1 -m -u -n -i \
    sysctl -w vm.max_map_count=262144