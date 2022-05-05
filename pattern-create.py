#!/usr/bin/env python3

import sys
import argparse
from struct import pack

def pattern_create(length = 8192):
    pattern = ''
    parts = ['A', 'a', '0']

    while len(pattern) != length:
        pattern += parts[len(pattern) % 3]
        if len(pattern) % 3 == 0:
            parts[2] = chr(ord(parts[2]) + 1)
            if parts[2] > '9':
                parts[2] = '0'
                parts[1] = chr(ord(parts[1]) + 1)
                if parts[1] > 'z':
                    parts[1] = 'a'
                    parts[0] = chr(ord(parts[0]) + 1)
                    if parts[0] > 'Z':
                        parts[0] = 'A'

    return pattern

def pattern_offset(value, length=8192):
    pattern = pattern_create(length)

    try:
        return pattern.index(value)
    except ValueError:
        return 'Not found!'

def main():
    parser = argparse.ArgumentParser(prog='pattern', usage='%(prog)s [-c length | offset [subpattern length]]')
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "-c", "--create", help="Create a pattern with the given length")
    group.add_argument(
        "-o", "--offset", nargs='+', help="Find the offset of the given subpattern")
    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)

    if args.create:
        if args.create.startswith('0x'):
            length = int(args.create, 16)
        else:
            length = int(args.create)

        if length  < 1:
            print("[-] Error: length must be >= 1")
            sys.exit(1)

        print(pattern_create(length))

    if args.offset:
        if len(args.offset) > 2:
            print("[-] Error: this option accepts up to 2 arguments")
            sys.exit(1)

        value = args.offset[0]
        if value.startswith('0x'):
            try:
                value = pack('<I', int(value, 16)).decode("utf-8").strip('\x00')
            except:
                value = pack('<Q', int(value, 16)).decode("utf-8").strip('\x00')
                
        if len(args.offset) == 1:
            print(pattern_offset(value))
        else:
            print(pattern_offset(value, int(args.offset[1])))

if __name__ == '__main__':
    main()