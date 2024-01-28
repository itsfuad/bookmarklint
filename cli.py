#!/usr/bin/env python3
"""Command-line interface for bookmarklint."""
import argparse
import json
import sys
from bookmarklint import analyze

def main(argv=None):
    parser = argparse.ArgumentParser(description='Audit exported bookmark URL lists for duplicates and invalid schemes')
    parser.add_argument('path', help='Input data file, or - for standard input')
    args = parser.parse_args(argv)
    if args.path == '-':
        data = sys.stdin.read()
    else:
        with open(args.path, encoding='utf-8') as f:
            data = f.read()
    print(json.dumps(analyze(data), sort_keys=True))
    return 0

if __name__ == '__main__':
    sys.exit(main())
