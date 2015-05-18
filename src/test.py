# -*- coding: utf-8 -*-

import re

def test(line):
    pattern = ['[^a-zA-Z \n.,;:]+',
               '[ ,.:;][a-zA-Z],[a-zA-Z][ ,.:;]',
               '^[a-zA-Z],[a-zA-Z][ \n,.:;]',
               '[ ,.:;][a-zA-Z],[a-zA-Z]\n',
               '[ ,.:;][a-zA-Z][ ,.:;]',
               '^[a-zA-Z][ \n,.:;]',
               '[ ,.:;][a-zA-Z]\n']
            
    # non-letter or punctuation
    line = re.sub(pattern[0], "", line)
    # subscript in the middle of line
    line = re.sub(pattern[1], " ", line)
    # subscript at the start of line
    line = re.sub(pattern[2], "", line)
    # subscript at the end of line
    line = re.sub(pattern[3], "", line)
    # single letter in the middle of line
    line = re.sub(pattern[4], " ", line)
    # single letter at the start of line
    line = re.sub(pattern[5], "", line)
    # single letter at the end of line
    line = re.sub(pattern[6], "", line)
    
    print line
    
    return

if __name__ == "__main__":
    
    test("w\n")
