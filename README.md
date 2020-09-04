# spell.py
Spells text using (phonetic) alphabet(s)

### Usage:

    python3 spell.py [-h] [--dict DICT] [--text TEXT]

### Optional arguments:

    -h, --help   show this help message and exit
  
    --dict DICT  custom dictionary (in JSON format)
  
    --text TEXT  text to be spelled, if omitted spells from the standard input

### Examples:

To spell the text "Hello" using Morse code, use

    python3 spell.py --dict="Morse.json" --text="Hello"

To spell using the default NATO phonetic dictionary, use

    python3 spell.py --text="Hello"

To spell directly from the console using the default NATO phonetic dictionary, use

    python3 spell.py

then start typing. `spell.py` accepts UNIX-like piping, e.g. type
    
    cat some_file.txt | python3 spell.py

to spell the content of `some_file.txt`.
    
### Creating custom dictionaries

You can create your own custom dictionary in JSON format, see `NATO.json` or 
`Morse.json` for details.
