#!/us/bin/env python
import sys, time

def parseRecords():
    for line in sys.stdin:
        line = line.strip('\n')
        line = line.split(',')
        yield int(line[2])/60

def mapper():
    for words in parseRecords():
        print '%s\t%s' % (words, 1)

if __name__=='__main__':
    mapper()