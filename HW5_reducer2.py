#!/us/bin/env python
import intertools, operator, sys

def parsePairs():
    for line in sys.stdin:
        kv = line.strip('\n').split('\t')
        yield (int(kv[0]), int(kv[1]))

def reducer():
    minutes = {}
    curSum = 0
    total = 0
    for key, pairs in itertools.groupby(parsePairs(), operator.itemgetter(0)):
        minutes[int(key)] = [int(i[1]) for i in pairs][0]
    total = sum(minutes.values())
    for i in sorted(minutes.key()):
        curSum += minutes[i]
        if curSum >= total/2.0:
            print i
            break

if __name__=='__main__':
    reducer()