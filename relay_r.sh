#!/usr/bin/env bash
set -ex

ssh -i ~/.ssh/bloxroute_test ec2-user@54.91.141.111 "python relay.py 8080 34.207.201.85 8080 34.230.34.244 8080 54.226.36.1 8080" &