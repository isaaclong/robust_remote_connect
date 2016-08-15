#! /usr/bin/python3
import argparse
import time
import os
import sys
from subprocess import Popen, call, PIPE
import re
import ipaddress

parser = argparse.ArgumentParser(description='todo')

parser.add_argument('cloud_username', type=str, help='username to SSH into for cloud box')

parser.add_argument('cloud_ip', type=ipaddress.ip_address, help='IP address of cloud box')

args = parser.parse_args()

os.environ["AUTOSSH_GATETIME"] = "0"
os.environ["AUTOSSH_POLL"] = "60" # poll for a connection every 60 seconds

autossh_cmd = ["autossh", args.cloud_username + "@" + str(args.cloud_ip), "-R", "0:localhost:22", "sleep"]
print(" ".join(autossh_cmd))
autossh_process = Popen(autossh_cmd, stdout=PIPE, shell=True)

for line in autossh_process.stdout:
    match = re.search("Allocated port ([0-9]*)", line)
    if match:
        port = match.group(1)
        call(["autossh", args.cloud_username + "@" + args.cloud_ip, "set_port", "--port", port]) # automatically retries on poor connection
