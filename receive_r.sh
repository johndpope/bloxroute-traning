#!/usr/bin/env bash
set -ex

ssh -i ~/.ssh/bloxroute_test ec2-user@34.207.201.85 "python receiver.py 0.0.0.0 8080" &
ssh -i ~/.ssh/bloxroute_test ec2-user@34.230.34.244 "python receiver.py 0.0.0.0 8080" &
ssh -i ~/.ssh/bloxroute_test ec2-user@54.226.36.1 "python receiver.py 0.0.0.0 8080" 