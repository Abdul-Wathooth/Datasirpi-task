#!/bin/bash

cd ~/Datasirpi-task/webhook-docker

git pull origin main

docker stop demo-container || true
docker rm demo-container || true

docker build -t demo-app .

docker run -d -p 5000:5000 --name demo-container demo-app
