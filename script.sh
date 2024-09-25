#!/bin/sh

git clone https://github.com/RampageWallE/DAEA-examen-1.git app

cd app 

docker compose up -d --build 

./script.sh