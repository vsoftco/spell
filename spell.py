#!/usr/bin/env python3
#
# spell.py
#
# Spells text using phonetic alphabet(s)
# Use python3 spell.py -h for help
#
# MIT License
#
# Copyright (c) 2013 - 2018 Vlad Gheorghiu (vgheorgh@gmail.com)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import argparse
import json
import sys

# Default dictionary
dictionary = {'A': "Alpha", 'B': "Bravo", 'C': "Charlie", 'D': "Delta",
              'E': "Echo", 'F': "Foxtrot", 'G': "Golf", 'H': "Hotel",
              'I': "India", 'J': "Juliet", 'K': "Kilo", 'L': "Lima",
              'M': "Mike", 'N': "November", 'O': "Oscar", 'P': "Papa",
              'Q': "Quebec", 'R': "Romeo", 'S': "Sierra", 'T': "Tango",
              'U': "Uniform", 'V': "Victor", 'W': "Whiskey", 'X': "X-ray",
              'Y': "Yankee", 'Z': "Zulu"}


# Spells a string using a specified dictionary
def spell(string, dic):
    for char in string:
        up_char = char.upper()
        if up_char in dic:
            print(('{key} - {value}'.format(key=char, value=dic[up_char])).rstrip())
        else:
            print(char.rstrip())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Spells text using phonetic alphabet(s)')
    parser.add_argument('--dict', help='custom dictionary (in JSON format)')
    parser.add_argument('--text', help='text to be spelled, if omitted spells from the standard input')
    args = parser.parse_args()

    # We have a custom dictionary
    if args.dict is not None:
        try:
            with open(args.dict, 'rt') as f:
                try:
                    dictionary = json.load(f)
                except json.decoder.JSONDecodeError:
                    print('Cannot parse the dictionary "{dict}"'.format(dict=args.dict))
                    exit(-1)
        except IOError:
            print('Cannot open the dictionary "{dict}"'.format(dict=args.dict))
            exit(-1)

    # We have text passed from the command line
    if args.text is not None:
        spell(args.text, dictionary)
    # We have text taken from the standard input
    else:
        while True:
            line = sys.stdin.readline()
            if line == '':
                break
            spell(line, dictionary)
