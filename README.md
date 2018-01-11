# spell
Spells text using phonetic alphabet(s)

# Usage:

    `python3 spell.py [-h] [--dict DICT] [--text TEXT]`

# Optional arguments:

  `-h, --help`   show this help message and exit
  
  `--dict DICT`  custom dictionary (in JSON format)
  
  `--text TEXT`  text to be spelled, if omitted spells from the standard input

# Example:

To spell the text "Hello" using Morse code, use

    `python3 spell.py --dict="Morse.json" --text="Hello"`

To spell using the default NATO phonetic dictionary, use

    `python3 spell.py --text="Test"`

The following spells a text file via UNIX-like piping using the default NATO phonetic dictionary
    
    `cat some_file.txt | python3 spell.py`


