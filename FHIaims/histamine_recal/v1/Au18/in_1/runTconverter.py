import re
import sys
f = open("runTtemp.sh", "w")

mylines = []
mydata = []
myseconddata = []
moveddata = []
titleline = []
linenum=0
startindex = 0
endindex = 0
itemnum = 0
#stepnum=str(1)
stepnum = str(sys.argv[1])
#nelectrodeL = int(sys.argv[2])
#nLrelax = int(sys.argv[3])
#nelectrodeR = int(sys.argv[4])
#nRrelax = int(sys.argv[5])
#InorOut = sys.argv[6]


with open ("runT.sh", "rt") as myfile:
    for myline in myfile:
        linenum += 1
        mylines.append(myline.rstrip('\n'))
        substra = "ACTIVE=/projectnb/kamenet/xiaoyun/FHIaims/histamine_recal/v1/Au18/in_1/"
        #print(myline)
        #linenum = len(myfile)-1
        if myline.find(substra) != -1:
            endindex = linenum
            #print(startindex)
        else:
            continue
    linenum = 0
    for myline in mylines:
        linenum += 1
        if linenum == endindex:
            mydata.append("ACTIVE=/projectnb/kamenet/xiaoyun/FHIaims/histamine_recal/v1/Au18/in_1/step%s" % stepnum) 
        else:
            mydata.append(myline)
      

    for item in mydata:
        f.writelines("%s\n" % item)
    f.close()
    
    


