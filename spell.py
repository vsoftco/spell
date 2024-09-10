#!/usr/bin/env python3

# spell.py
#
# Spells text using various alphabets. By default, uses the NATO phonetic
# alphabet.
#
# Execute
#     python3 spell.py --help
# for help

# Copyright (c) 2018 - 2024 Vlad Gheorghiu. All rights reserved.
#
# MIT License
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
def spell(string, dict):
    for char in string:
        if char in dict:
            print("{key} | {value}".format(key=char, value=dict[char]))
        elif char.upper() in dict:
            print("{key} | {value}".format(key=char, value=dict[char.upper()]))
        elif char.lower() in dict:
            print("{key} | {value}".format(key=char, value=dict[char.lower()]))
        elif char == "\n":
            print("----- newline -----")
        else:
            print(char)


# Loads a custom dictionary
def load_dict(path):
    try:
        with open(path, "rt") as f:
            return json.load(f)
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error loading dictionary '{path}': {e}")
        sys.exit(-1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Spells text using phonetic alphabet(s)"
    )
    parser.add_argument("-d", "--dict", help="custom dictionary (in JSON format)")
    parser.add_argument(
        "text",
        nargs="?",
        help="text to be spelled, if omitted spells from the standard input",
    )
    args = parser.parse_args()

    dictionary = (
        load_dict(args.dict)
        if args.dict
        else {
            "a": "Alpha",
            "b": "Bravo",
            "c": "Charlie",
            "d": "Delta",
            "e": "Echo",
            "f": "Foxtrot",
            "g": "Golf",
            "h": "Hotel",
            "i": "India",
            "j": "Juliet",
            "k": "Kilo",
            "l": "Lima",
            "m": "Mike",
            "n": "November",
            "o": "Oscar",
            "p": "Papa",
            "q": "Quebec",
            "r": "Romeo",
            "s": "Sierra",
            "t": "Tango",
            "u": "Uniform",
            "v": "Victor",
            "w": "Whiskey",
            "x": "X-ray",
            "y": "Yankee",
            "z": "Zulu",
            "1": "One",
            "2": "Two",
            "3": "Three",
            "4": "Four",
            "5": "Five",
            "6": "Six",
            "7": "Seven",
            "8": "Eight",
            "9": "Nine",
            "0": "Zero",
        }
    )

    # Text from the command line, or from the standard input
    # If from standard input, stops on CTRL+D (UNIX) or CTRL+Z (Windows)
    text = args.text or sys.stdin
    try:
        for line in text:
            spell(line, dictionary)
    except (KeyboardInterrupt, EOFError):
        sys.exit()
