#!/usr/bin/env python3
#
# spell.py
#
# Spells text using various alphabets. By default, uses the NATO phonetic
# alphabet.
#
# Type python3 spell.py -h for help
#
# MIT License
#
# Copyright (c) 2018 - 2020 Vlad Gheorghiu.
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


# Spells a string using a specified dictionary
def spell(string, dic):
    for char in string:
        if char in dic:
            print('{key} | {value}'.format(key=char, value=dic[char]))
        elif char.upper() in dic:
            print('{key} | {value}'.format(key=char, value=dic[char.upper()]))
        elif char.lower() in dic:
            print('{key} | {value}'.format(key=char, value=dic[char.lower()]))
        elif char == '\n':
            print("----- newline -----")
        else:
            print(char)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Spells text using phonetic alphabet(s)')
    parser.add_argument('--dict', help='custom dictionary (in JSON format)')
    parser.add_argument('--text', help='text to be spelled, if omitted spells from the standard input')
    args = parser.parse_args()

    # Custom dictionary
    if args.dict is not None:
        try:
            with open(args.dict, 'rt') as f:
                try:
                    dictionary = json.load(f)
                except json.decoder.JSONDecodeError as json_exception:
                    print("Cannot parse the dictionary '{dict}'".format(dict=args.dict))
                    print(json_exception)
                    sys.exit(-1)
        except IOError as io_exception:
            print("Cannot open the dictionary '{dict}'".format(dict=args.dict))
            print(io_exception)
            sys.exit(-1)
    else:
        # Use the NATO phonetic dictionary by default
        dictionary = {'A': "Alpha", 'B': "Bravo", 'C': "Charlie", 'D': "Delta",
                      'E': "Echo", 'F': "Foxtrot", 'G': "Golf", 'H': "Hotel",
                      'I': "India", 'J': "Juliet", 'K': "Kilo", 'L': "Lima",
                      'M': "Mike", 'N': "November", 'O': "Oscar", 'P': "Papa",
                      'Q': "Quebec", 'R': "Romeo", 'S': "Sierra", 'T': "Tango",
                      'U': "Uniform", 'V': "Victor", 'W': "Whiskey", 'X': "X-ray",
                      'Y': "Yankee", 'Z': "Zulu", '1': "One", '2': "Two",
                      '3': "Three", '4': "Four", '5': "Five", '6': "Six",
                      '7': "Seven", '8': "Eight", '9': "Nine", '0': "Zero"}

    # Text passed from the command line
    if args.text is not None:
        spell(args.text, dictionary)
    else:
        # We have text taken from the standard input
        while True:
            line = sys.stdin.readline()
            # Stops on CTRL+D (UNIX) or CTRL+Z (Windows)
            if line == '':
                break
            spell(line, dictionary)
