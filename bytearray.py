#!/usr/bin/env python3
import sys

excluded = set(bytes.fromhex(sys.argv[1].replace("\\x", ""))) if len(sys.argv) > 1 else set()

byte_array = bytes(x for x in range(256) if x not in excluded)

sys.stdout.buffer.write(byte_array)

