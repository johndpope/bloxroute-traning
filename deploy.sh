#!/usr/bin/env bash
set -ex

scp -i ~/.ssh/bloxroute_test /Users/Sergey/Documents/Projects/BloXroute/training/receiver.py ec2-user@54.146.113.165:
scp -i ~/.ssh/bloxroute_test /Users/Sergey/Documents/Projects/BloXroute/training/receiver.py ec2-user@52.71.252.240:
scp -i ~/.ssh/bloxroute_test /Users/Sergey/Documents/Projects/BloXroute/training/receiver.py ec2-user@54.152.196.152:

scp -i ~/.ssh/bloxroute_test /Users/Sergey/Documents/Projects/BloXroute/training/relay.py ec2-user@18.232.71.160:

scp -i ~/.ssh/bloxroute_test /Users/Sergey/Documents/Projects/BloXroute/training/sender.py ec2-user@18.207.229.31:


