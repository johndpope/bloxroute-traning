#!/usr/bin/env bash
set -ex

python receiver.py 0.0.0.0 8080 &
python receiver.py 0.0.0.0 8081 &
python receiver.py 0.0.0.0 8082 &

