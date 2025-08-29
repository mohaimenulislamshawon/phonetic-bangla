# In: src/phoneticbn/cli.py

import sys
from .engine import transliterate

def main():
    """Entry point for the command-line tool."""
    if len(sys.argv) > 1:
        input_text = " ".join(sys.argv[1:])
        output_text = transliterate(input_text)
        print(output_text)
    else:
        print("Usage: phonetic-bangla <phonetic english text>")
        print("Example: phonetic-bangla amar shonar bangla")
