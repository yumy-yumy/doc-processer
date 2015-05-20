import re


def dataToFile(data_iterator, fname):
    """Function which writes each line to the file"""
    with open(fname, 'wb') as fileWriter:
        for line in data_iterator:
            fileWriter.write(line)
    print "finish"
    return 

def dataFromFile(fname):
        """Function which reads from the file, removes non-words and yields a generator"""
        pattern = ['\$.*?\$',
                   '\-\s*[0-9]+',
                   '[0-9]+\s*\-',
                   '([a-zA-Z0-9\_\^]+\s*[\+\*\/\=\>\<\%]\s*)+[a-zA-Z0-9\_\^]+',
                   '\[[0-9]+\]',
                   '\\[a-zA-Z]+']
        file_iter = open(fname, 'rU')
        for line in file_iter:
            #print line
            line = line.replace('(', '')
            line = line.replace(')', '')
            line = line.replace('{', '')
            line = line.replace('}', '')
            
            # equation
            line = re.sub(pattern[0], "", line)
            # negative sign
            line = re.sub(pattern[1], "1", line)
            # minus formula with number
            line = re.sub(pattern[2], "1", line)
            # formula except minus
            line = re.sub(pattern[3], "", line)
            # citation
            line = re.sub(pattern[4], "", line)
            # latex keywords
            line = re.sub(pattern[5], "", line)

            #print line
            #input()
            yield line    
