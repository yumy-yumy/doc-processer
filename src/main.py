# -*- coding: utf-8 -*-

import sys
from optparse import OptionParser
import prePdf 


if __name__ == "__main__":
    
    optparser = OptionParser()
    optparser.add_option('-f', '--inputFile',
                         dest='input',
                         help='filename containing txt',
                         default=None)

    (options, args) = optparser.parse_args()
    
    inFile = None
    if options.input is None:
            inFile = sys.stdin
    elif options.input is not None:
            inFile = prePdf.dataFromFile(options.input)
    else:
            print 'No filename specified, system with exit\n'
            sys.exit('System will exit')
            
    fileName = "data.txt"
    prePdf.dataToFile(inFile, fileName)
