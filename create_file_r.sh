#!/usr/bin/env bash
set -ex

ssh -i ~/.ssh/bloxroute_test ec2-user@18.207.229.31 "rm transfer.txt"
ssh -i ~/.ssh/bloxroute_test ec2-user@18.207.229.31 "head -c 3G </dev/urandom >transfer.txt"
