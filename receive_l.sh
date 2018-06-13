#!/usr/bin/env bash
set -ex

python receiver.py 0.0.0.0 8090 &
python receiver.py 0.0.0.0 8091 &
python receiver.py 0.0.0.0 8092 &

