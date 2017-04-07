#Takes input from 4 files, 'UseableCValues.txt', 'UseableSValues.txt', 'UseableDValues.txt', 'AllValues.txt' (output from findCSD.py) and generates 4 networks - one for each of the C/S/D-type interactions, as well as an aggregate network containing all 3

#Outputs selected pairs, along with metric type and value, to SelectedSNodes.txt, SelectedCNodes.txt, SelectedDNodes.txt, and CSDSelection.txt


##############################################
#Parameters to vary are selSize and noSels

#selSize indicates approximate proportion of selected nodes, being equal to the 1/(desired p-value). Increasing selSize selects fewer edges. 
#noSels may be increased as desireable, at the expense of longer running time. May also be decreased, at the expense of accuracy


import math
import numpy
import random

selSize = 100000
noSels = 10000


cValueFile = 'UseableCValues.txt'
sValueFile = 'UseableSValues.txt'
dValueFile = 'UseableDValues.txt'

f = open(cValueFile)

valueList = []

for line in f:
    valueList.append(float(line))


cutoffAtSel = []
for i in range(noSels):

    selection = [valueList[i] for i in random.sample(xrange(0, len(valueList)), selSize)]
    cutoffAtSel.append(max(selection))

cCutoff = numpy.mean(cutoffAtSel)

f.close()



f = open(sValueFile)

valueList = []

for line in f:
    valueList.append(float(line))


cutoffAtSel = []
for i in range(noSels):

    selection = [valueList[i] for i in random.sample(xrange(0, len(valueList)), selSize)]
    cutoffAtSel.append(max(selection))

sCutoff = numpy.mean(cutoffAtSel)
f.close()


f = open(dValueFile)

valueList = []

for line in f:
    valueList.append(float(line))


cutoffAtSel = []
for i in range(noSels):

    selection = [valueList[i] for i in random.sample(xrange(0, len(valueList)), selSize)]
    cutoffAtSel.append(max(selection))

dCutoff = numpy.mean(cutoffAtSel)
f.close()

cNetF = open('CNetwork.txt', 'w')
sNetF = open('SNetwork.txt', 'w')
dNetF = open('DNetwork.txt', 'w')
csdNetF = open('CSDSelection.txt', 'w')

f = open('AllValues.txt')

f.readline()

for line in f:

    splitLine = line.rstrip().split('\t')
    if float(splitLine[6]) > cCutoff:
        print >> cNetF, str(splitLine[0])+'\t'+str(splitLine[1])+'\t'+str(splitLine[6])+'\t'+'C'
        print >> csdNetF, str(splitLine[0])+'\t'+str(splitLine[1])+'\t'+str(splitLine[6])+'\t'+'C'

    if float(splitLine[7]) > sCutoff:
        print >> sNetF, str(splitLine[0])+'\t'+str(splitLine[1])+'\t'+str(splitLine[7])+'\t'+'S'
        print >> csdNetF, str(splitLine[0])+'\t'+str(splitLine[1])+'\t'+str(splitLine[7])+'\t'+'S'

    if float(splitLine[8]) > dCutoff:
        print >> dNetF, str(splitLine[0])+'\t'+str(splitLine[1])+'\t'+str(splitLine[8])+'\t'+'D'
        print >> csdNetF, str(splitLine[0])+'\t'+str(splitLine[1])+'\t'+str(splitLine[8])+'\t'+'D'



cNetF.close()
sNetF.close()
dNetF.close()
f.close()
