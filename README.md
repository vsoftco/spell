# spell.py
Spells text using various alphabets.
By default, uses the NATO phonetic alphabet.

### Usage:

    python3 spell.py [-h] [--dict DICT] [--text TEXT]

### Optional arguments:

    -h, --help   show this help message and exit
  
    --dict DICT  custom dictionary (in JSON format)
  
    --text TEXT  text to be spelled, if omitted spells from the standard input

### Examples:

To spell using the default NATO phonetic alphabet, use

    python3 spell.py --text="Hello"

To spell the text "Hello" using Morse code, use

    python3 spell.py --dict="Morse.json" --text="Hello"

To spell from the console using the default NATO phonetic alphabet, use

    python3 spell.py

then start typing (end with CTRL+D on UNIX-like systems).

`spell.py` accepts UNIX-like piping, e.g. type
    
    cat some_file.txt | python3 spell.py

to spell the content of `some_file.txt`.
    
### Creating custom dictionaries

You can create your own custom dictionary in JSON format, see `NATO.json` or 
`Morse.json` for details.
