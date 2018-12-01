#!/usr/bin/env bash
docker build -t automation-test .
docker run --rm -p 5904:25900 -p 4444:24444 -v "$(pwd)":/home/seluser/automation/myScript --name automation-container automation-test:latest