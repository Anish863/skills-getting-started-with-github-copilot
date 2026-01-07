#!/usr/bin/env python3
"""
Simple frequency counter.

Usage examples:
  echo "hello world hello" | python3 src/frequency_counter.py --mode word
  printf "ababa\n" | python3 src/frequency_counter.py --mode char --sort alpha
  python3 src/frequency_counter.py file.txt --mode line --top 10
"""

import sys
import argparse
from collections import Counter


def count_tokens(text, mode='word', ignore_case=False):
    if ignore_case:
        text = text.lower()
    if mode == 'word':
        tokens = text.split()
    elif mode == 'char':
        tokens = [c for c in text if not c.isspace()]
    elif mode == 'line':
        tokens = [line for line in text.splitlines() if line != '']
    else:
        raise ValueError('Unknown mode: ' + mode)
    return Counter(tokens)


def main():
    parser = argparse.ArgumentParser(description='Frequency counter')
    parser.add_argument('file', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
    parser.add_argument('--mode', choices=['word', 'char', 'line'], default='word')
    parser.add_argument('--top', type=int, default=0, help='Show only top N results (0 = all)')
    parser.add_argument('--ignore-case', action='store_true')
    parser.add_argument('--sort', choices=['freq', 'alpha'], default='freq', help='Sort by frequency or alphabetic')
    args = parser.parse_args()

    text = args.file.read()
    c = count_tokens(text, args.mode, args.ignore_case)
    items = list(c.items())
    if args.sort == 'freq':
        items.sort(key=lambda x: (-x[1], x[0]))
    else:
        items.sort(key=lambda x: x[0])

    if args.top:
        items = items[: args.top]

    for token, count in items:
        print(f"{token}\t{count}")


if __name__ == '__main__':
    main()