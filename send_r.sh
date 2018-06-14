#!/usr/bin/env bash
set -ex

ssh -i ~/.ssh/bloxroute_test ec2-user@18.207.229.31 "python sender.py transfer.txt 18.232.71.160 8080"