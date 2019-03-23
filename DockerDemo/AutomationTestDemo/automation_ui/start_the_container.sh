#!/usr/bin/env bash
docker build -t automation-test .
docker run --rm -p 5904:25900 -p 4444:24444 -v "$(pwd)":/home/seluser/automation/myScript --name automation-container automation-test:latest
docker run --rm -p 5904:25900 -p 4444:24444 --name automation-container -v "$(pwd)":/home/seluser/automation -e SCREEN_WIDTH=1024 -e SCREEN_HEIGHT=768 automationtest:latest