
import random
import sys


def main():

    final = []

    inputF = sys.argv[1]
    outputF = sys.argv[2]
   
    with open (inputF) as f:
        lis = f.readlines()
        for lines in lis:
            if len(lines.split()) == 0:
                continue
            else:
                tempLis = lines.split()
                tempLis = [int(i) for i in tempLis] 
                final = tempLis

    fin = [0] + final + [max(final) + 1]
    improvedBPR(fin, outputF)

def hasBP(final):

    for i in range (1, len(final)):
        if ( final[i] != final[i - 1] + 1):
            return True
    
    return False
       
def breakPoint(final):


    points = []

    for i in range (len(final) - 1):
        if ((abs(final[i+1] - final [i]) != 1)):
            points.append([i, i + 1])


    return points

def stripCheck(fin):

    increasing = []
    decreasing = []

    endC = 0
    
    for i in range (1, len(fin)):
        
        if ((abs(fin[i - 1] - fin[i]) != 1) and endC <= i - 1 ):

            if (i - 1 == 0):
                increasing.append([i - 1, i - 1])
            
            elif (i == (len(fin)) - 1 ):
                increasing.append([i - 1, i - 1])

            else:
                decreasing.append([i - 1, i - 1])

        
        if ((abs(fin[i - 1] - fin[i]) == 1) and endC <= i - 1):

            start = i - 1
            newStart = i
            newI = start 

            while (newStart + 1 < len(fin) and abs(fin[newStart] - fin[newStart + 1]) == 1):
                if (newStart + 1 < len(fin)):
                    newStart = newStart + 1
                else:
                    break

            end = newStart

            if (fin[start] < fin[end]):
                increasing.append([start, end])

            else:
                decreasing.append([start, end])

            endC = end + 1

            if (endC == len(fin) - 1):
                increasing.append([endC, endC])

    return increasing, decreasing

def decReversal(increasing, decreasing, final):

    if (len(decreasing) > 0):

        right = [j for i, j in decreasing]

        lowest = 0
        coord = 0
        start = 0
        index = 0
        realInd = 0
        for x in right:
            if (start == 0): 
                lowest = final[x]
                start = 1

            if (lowest > final[x]):
                lowest = final[x]
                coord = x
                realInd = index
            index = index + 1

        reversal = decreasing[realInd]

        revCoord = [0, 0]

        for i in range (len(final)):

            if (final[i] < final[reversal[1]] and abs(final[i] - final[reversal[1]]) == 1):
                reversalTo = i
    
        if (reversalTo > reversal[1]):
            revCoord = [reversal[1], reversalTo]
        else:
            revCoord = [reversalTo, reversal[1]]

    else:
        revCoord = [increasing[1][0] - 1, increasing[1][1]]

    first = final[:revCoord[0] + 1] 
    middlePart = final[revCoord[0] + 1: revCoord[1] +1]
    reverMiddle = middlePart[::-1]
    ending = final[revCoord[1] + 1:]

    finRever = first + reverMiddle + ending

    return finRever
    
def improvedBPR(final, outputF):

    outi = open(outputF, "w")
    outi.write("Original Sequence: " + str(final))
    
    outi.write("\n" + "Sorting Now\n")
    
    seq = final
    reversalD = 0
    while hasBP(seq):
        increasing, decreasing = stripCheck(seq)
        totalStrips = increasing + decreasing
        numBP = len(totalStrips) - 1
        outi.write("Number Of Break Points: " +  str(numBP) + "\n")
        seq = decReversal(increasing, decreasing, seq)
        reversalD = reversalD + 1

        outi.write( "Updated Seq: " + str(seq) + "\n")
        outi.write("")

    outi.write("Sorting Ended - Reversal Distance: " + str(reversalD) + '\n')
    outi.write("Final Sequence: " + str(seq))
    outi.close()
    
if __name__ == "__main__":
    main()
