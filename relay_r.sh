#!/usr/bin/env bash
set -ex

ssh -i ~/.ssh/bloxroute_test ec2-user@18.232.71.160 "python relay.py 8080 54.146.113.165 8080 52.71.252.240 8080 54.152.196.152 8080" &