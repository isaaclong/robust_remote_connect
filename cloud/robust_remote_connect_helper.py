#! /usr/bin/python3
import argparse
import time
import os
import sys

parser = argparse.ArgumentParser(description='Handle reporting ssh remote forwarding dynamic ports for field boxes.')

parser.add_argument('hostname', type=str, help='hostname of field box')

parser.add_argument('command', type=str, choices=["set_port", "sleep"], help='action to be taken')

parser.add_argument('--port', help='Port number on cloud machine ssh remote forwarded to a field box with the given hostname.')

args = parser.parse_args()

if args.command == "set_port":
    if args.port is None:
        print("Must use --port option to set port.")
    else:
        print("Setting port " + args.port + " for hostname " + args.hostname)
        ports_dir = "/tmp/remote_connect_ports"
        if not os.path.exists(ports_dir):
            os.mkdir(ports_dir)
        temp_port_filename = '/tmp/remote_connect_ports/.' + args.hostname + str(time.perf_counter())
        f = open(temp_port_filename, 'w')
        f.write(args.port)
        f.flush()
        os.fsync(f.fileno())
        f.close()

        proper_port_filename = '/tmp/remote_connect_ports/' + args.hostname
        os.rename(temp_port_filename, proper_port_filename)

if args.command == "sleep":
    print("Sleeping")
    while True:
        time.sleep(60)
