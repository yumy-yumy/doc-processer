import re
import string

def dataToFile(data_iterator, fname):
    """Function which writes each line to the file"""
    with open(fname, 'wb') as fileWriter:
        for line in data_iterator:
            if line != "" and line != "\n":
                fileWriter.write(line)
    print "finish"
    return 

def dataFromFile(fname):
    """Function which reads from the file, removes non-words and yields a generator"""
    pattern = ['[^a-zA-Z \n.,;:]+',
               '[ ,.:;][a-zA-Z],[a-zA-Z][ ,.:;]',
               '^[a-zA-Z],[a-zA-Z][ \n,.:;]',
               '[ ,.:;][a-zA-Z],[a-zA-Z]\n',
               '[ ,.:;][a-zA-Z][ ,.:;]',
               '^[a-zA-Z][ \n,.:;]',
               '[ ,.:;][a-zA-Z]\n']
    
    file_iter = open(fname, 'rU')
    for line in file_iter:
        
        print line
        
        line = filter(lambda x: x in string.printable, line)
            
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
    
        yield line
