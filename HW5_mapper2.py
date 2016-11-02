#!/us/bin/env python
import sys, time

def mapper():
    for line in sys.stdin:
        line = line.strip('\n')
        print line

if __name__=='__main__':
    mapper()