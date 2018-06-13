#!/usr/bin/env bash
set -ex

ssh -i ~/.ssh/bloxroute_test ec2-user@54.161.150.24 "python sender.py transfer.txt 54.91.141.111 8080"