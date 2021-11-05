from os import sys

def main():
    if not len(sys.argv) == 8:
        print("Usage: cacheSim latD latP latS capD capP n s")
        return
    try:
        latD = float(sys.argv[1])
        latP = float(sys.argv[2])
        latS = float(sys.argv[3])
        capD = float(sys.argv[4])
        capP = float(sys.argv[5])
        n = int(sys.argv[6])
        s = float(sys.argv[7])
    except:
        print("cacheSim: invalid arguments")
        return
    try:
        print(cacheSim(latD, latP, latS, capD, capP, n, s))
    except:
        print("cacheSim: error while calculating")
        return
    
def cacheSim(latD, latP, latS, capD, capP, n, s):
    def zipF(a, b):
        return 1 / (a ** b)
    totalTwo = 0
    totalThree = 0
    for i in range(1, n + 1):
        freq = zipF(i, s)
        #two layer aggreation
        if i <= capD:
            totalTwo += freq
        elif i <= capD + capP:
            totalTwo += freq * (latP / latD)
        else:
            totalTwo += freq * (1 + (latS / latD))
        #three layer aggregation
        if i <= capD:
            totalThree += freq
        elif i <= capP:
            totalThree += freq * (1 + (latP / latD))
        else:
            totalThree += freq * (1 + (latP / latD) + (latS / latD))
    return totalThree / totalTwo

if __name__ == "__main__":
    main()