import re

def test(line):
    pattern = ['([a-zA-Z0-9\_\^]+\s*[\+\*\/\=\>\<\%]\s*)+[a-zA-Z0-9\_\^]+',
               '\$.*?\$']
    line = re.sub(pattern[0], "", line)
    line = re.sub(pattern[1], "", line, re.I)
    line = line.replace('$', "")
    if line != "":
        print line
    else:
        print "null"    
    
    return



if __name__ == "__main__":
    
    test("$abc$anc$k$end")