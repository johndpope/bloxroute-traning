#!/usr/bin/env bash
set -ex

scp -i ~/.ssh/bloxroute_test /Users/Sergey/Documents/Projects/BloXroute/training/receiver.py ec2-user@34.207.201.85:
scp -i ~/.ssh/bloxroute_test /Users/Sergey/Documents/Projects/BloXroute/training/receiver.py ec2-user@34.230.34.244:
scp -i ~/.ssh/bloxroute_test /Users/Sergey/Documents/Projects/BloXroute/training/receiver.py ec2-user@54.226.36.1:

scp -i ~/.ssh/bloxroute_test /Users/Sergey/Documents/Projects/BloXroute/training/sender.py ec2-user@54.161.150.24:

scp -i ~/.ssh/bloxroute_test /Users/Sergey/Documents/Projects/BloXroute/training/relay.py ec2-user@54.91.141.111:
