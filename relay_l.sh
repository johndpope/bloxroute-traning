#!/usr/bin/env bash
set -ex

python relay.py 8083 0.0.0.0 8080 0.0.0.0 8081 0.0.0.0 8082 &