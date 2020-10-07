import re
import csv
import sys

arg1 = sys.argv[1]
arg2 = sys.argv[2]

def findClustersSmall(a):
    with open(a, "r") as f:
        AGATCcount = 0
        AATGcount = 0
        TATCcount = 0
        counter = 0
        dna = list(f.read())
        for x in dna:
            if dna[counter] == "A":
                if dna[counter + 1] == "G" and dna[counter + 2] == "A" and dna[counter + 3] == "T" and dna[counter + 4] == "C":
                    AGATCcount += 1
            if dna[counter] == "A":
                if dna[counter + 1] == "A" and dna[counter + 2] == "T" and dna[counter + 3] == "G":
                    AATGcount += 1
            if dna[counter] == "T":
                if dna[counter + 1] == "A" and dna[counter + 2] == "T" and dna[counter + 3] == "C":
                    TATCcount += 1
            counter += 1
        results = [str(AGATCcount), str(AATGcount), str(TATCcount)]
        return results

def findClustersLarge(a):
    with open(a, "r") as f:
        AGATCcount = 0
        TTTTTTCTcount = 0
        AATGcount = 0
        TCTAGcount = 0
        GATAcount = 0
        TATCcount = 0
        GAAAcount = 0
        TCTGcount = 0
        counter = 0
        dna = list(f.read())
        for x in dna:
            if dna[counter] == "A":
                if dna[counter + 1] == "G" and dna[counter + 2] == "A" and dna[counter + 3] == "T" and dna[counter + 4] == "C":
                    AGATCcount += 1
            if dna[counter] == "T":
                if dna[counter + 1] == "T" and dna[counter + 2] == "T" and dna[counter + 3] == "T" and dna[counter + 4] == "T" and dna[counter + 5] == "T" and dna[counter + 6] == "C" and dna[counter + 7] == "T":
                    TTTTTTCTcount += 1
            if dna[counter] == "A":
                if dna[counter + 1] == "A" and dna[counter + 2] == "T" and dna[counter + 3] == "G":
                    AATGcount += 1
            if dna[counter] == "T":
                if dna[counter + 1] == "C" and dna[counter + 2] == "T" and dna[counter + 3] == "A" and dna[counter + 4] == "G":
                    TCTAGcount += 1
            if dna[counter] == "G":
                if dna[counter + 1] == "G" and dna[counter + 2] == "A" and dna[counter + 3] == "T" and dna[counter + 4] == "A":
                    GATAcount += 1
            if dna[counter] == "T":
                if dna[counter + 1] == "A" and dna[counter + 2] == "T" and dna[counter + 3] == "C":
                    TATCcount += 1
            if dna[counter] == "G":
                if dna[counter + 1] == "A" and dna[counter + 2] == "A" and dna[counter + 3] == "A":
                    GAAAcount += 1
            if dna[counter] == "T":
                if dna[counter + 1] == "C" and dna[counter + 2] == "T" and dna[counter + 3] == "G":
                    TCTGcount += 1
            counter += 1
        results = [str(AGATCcount), str(TTTTTTCTcount), str(AATGcount), str(TCTAGcount), str(GATAcount), str(TATCcount), str(GAAAcount), str(TCTGcount)]
        return results

def findPerson(a,b):

    if str(b) == "dna/databases/small.csv":
        with open(b, "r") as f:
            reader = csv.DictReader(f)
            noMatchCount = 0
            for row in reader:
                if a[0] == row["AGATC"] and a[1] == row["AATG"] and a[2] == row["TATC"]:
                    print(row["name"])
                else:
                    noMatchCount += 1
            if noMatchCount == 3:
                print("No match")
                
    elif str(b) == "dna/databases/large.csv":
        with open(b, "r") as f:
            reader = csv.DictReader(f)
            noMatchCount = 0
            for row in reader:
                if a[0] == row["AGATC"] and a[1] == row["TTTTTTCT"] and a[2] == row["AATG"] and a[3] == row["TCTAG"] and a[4] == row["GATA"] and a[5] == row["TATC"] and a[6] == row["GAAA"] and a[7] == row["TCTG"]:
                    print(row["name"])
                else:
                    noMatchCount += 1
            if noMatchCount == 23:
                print("No match")  

findPerson((findClustersSmall(arg1)), arg2)