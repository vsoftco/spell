# spell.py
Spells text using various alphabets.
By default, uses the NATO phonetic alphabet.

### usage:

    python3 spell.py [-h] [-d DICTIONARY] [text]

### positional arguments:

    text                  text to be spelled, if omitted spells from the standard input

### optional arguments:

    -h, --help            show this help message and exit 
    -d DICT, --dict DICT  custom dictionary (in JSON format)
  
### Examples:

To spell using the default NATO phonetic alphabet, use

    python3 spell.py Hello 

To spell the text "Hello" using Morse code, use

    python3 spell.py -d Morse.json Hello

To spell from the standard input using the default NATO phonetic alphabet, use

    python3 spell.py

then start typing (end with CTRL+D on UNIX-like systems).

`spell.py` accepts UNIX-like piping, e.g., type
    
    cat some_file.txt | python3 spell.py # or python3 spell.py < some_file.txt

to spell the content of `some_file.txt`.
    
### Creating custom dictionaries

You can create your own custom dictionary in JSON format, see `NATO.json` or 
`Morse.json` for details.
