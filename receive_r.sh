#!/usr/bin/env bash
set -ex

ssh -i ~/.ssh/bloxroute_test ec2-user@54.146.113.165 "python receiver.py 0.0.0.0 8080" &
ssh -i ~/.ssh/bloxroute_test ec2-user@52.71.252.240 "python receiver.py 0.0.0.0 8080" &
ssh -i ~/.ssh/bloxroute_test ec2-user@54.152.196.152 "python receiver.py 0.0.0.0 8080" 