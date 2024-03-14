#!/usr/bin/env python
# this line means that the script is executable,
# it calls the language interpreter to run the code inside the script
# and is the guide to find 'python'


# import the module for reading and writing data
import sys

# input is read by STDIN (standard input) and do the following for each
# input line
keywords = ['career','need','feel','workplace','means','helps','create','business','information','read',
            'years','article','better','bored','world','feeling','remarkable','motion','enough','own',
            'experience','life','selfish','culture','because','generous','important','talking','entrepreneurship',
            'registry','effective','working','perseverance','people','time','people','community','choose',
            'entrepreneur','great','before','resilient','forward','available','employees','progress','companies',
            'work','episode','bizarre']

for fileline in sys.stdin:
    
    # remove leading and trailing whitespace
    fileline = fileline.strip()

    # split the line by space separator, a list is produced
    filewords = fileline.split(" ")
    
    for word in filewords:
        if word.lower() in keywords:
            print ('%s\t%s' % (word, 1))