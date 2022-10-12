import re
import sys
import os
import numpy as np
f = open("Energies.txt", "w")
g = open("Transmissions.txt", "w")

mylines = []
mylinesb = []
mydata = []
mydatab = []
myfile = []
mylisty = []
mylistyb = []
mylistyc = []
templisty = []
linenum=0
flagvar = True
path = str(os.getcwd())
nsteps = sys.argv[1]

strnsteps = str(nsteps)
#print(strnsteps)


i = 1
for i in range(1,int(nsteps)):
  linenum = 0
  mylines.clear()
  mylinesb.clear()
  mydata.clear()
  mylisty.clear()
  mylistyb.clear()  
  mylistyc.clear()
  stri = str(i)
  pathb = '/projectnb/kamenet/xiaoyun/FHIaims/histamine_recal/v1/Au18/in_1/step%s' % stri
  #print(pathb)
  os.chdir(pathb)
  pathc = os.getcwd()
  #print(pathc)
  with open ("TE.dat", "rt") as myfile:
  
    for myline in myfile:
      linenum += 1
      if linenum >= 4:
        mylines.append(myline.rstrip('\n'))
    linenum = 0
    
    for myline in mylines:
      strold = mylines[linenum]
      strnew = strold.replace('    ',',')
      strnew = strnew.replace(' ','')
      #print(strnew)
      mylines[linenum] = strnew
      linenum += 1
    
    itemnum = 0
    for myline in mylines:
      stra = mylines[itemnum]
      templisty = stra.split(",")
      #templisty = templisty.replace(" ","")
      #print(templisty)
      mylisty =  mylisty + templisty
      itemnum += 1
     
    #print(len(mylisty))
    mylisty.pop()
    mylisty.pop()
    leny = len(mylisty)
    
    itemnum = 0
    itemnumb = 1
    for item in mylisty:
      itemnumb += 3
      itemnum += 1
      #print(itemnumb)
      if  itemnumb < leny:
        strb = mylisty[itemnumb]
        #print(strb)
        flt = float(strb)
        mylistyb.append(flt)
      else:
        flagvar = False


    itemnum = 0
    itemnumb = 2
    for item in mylisty:
      itemnumb += 3
      itemnum += 1
      if  itemnumb < leny:
        strb = mylisty[itemnumb]
        #print(strb)
        flt = float(strb)
        mylistyc.append(flt)
      else:
        flagvar = False
    
    
    #print(mylistyb)
    #print(mylistyc)
    
    
    itemnum=0
    for item in mylistyb:
      fltb = mylistyb[itemnum]
      if fltb < 0.0:
        startindex = itemnum
      else:
        flagvar = False
      itemnum += 1
    itemnum = startindex + 1
    endindex = itemnum
    
    #print(startindex)
    #print(endindex)
    
    
    belowzerox = mylistyb[startindex]
    abovezerox = mylistyb[endindex]

    belowzeroy = mylistyc[startindex]
    abovezeroy = mylistyc[endindex]    
    
    #print(belowzerox)
    #print(belowzeroy)
    #print(abovezerox)
    #print(abovezeroy)        
    
    
    slopey = (abovezeroy - belowzeroy)/(abovezerox - belowzerox)
    
    inty = abovezeroy - slopey*abovezerox
    
    g.writelines("%f\n" % inty)

    linenum = 0
    startindexc= 0
    with open ("aims.dft.out", "rt") as myfileb:
      for myline in myfileb:
        #print(myline)
        mylinesb.append(myline.rstrip('\n'))
        #substra = "The following output summarizes some interesting total energy values"
        #substrb = "Final output of selected total energy values:"
        #if myline.find(substra) != -1:
        #    startindexc = linenum + 3
        #    print(startindexc)
        #else:
        #    continue
        #linenum += 1
        
      for myline in mylinesb:
        substra = "The following output summarizes some interesting total energy values"
        if myline.find(substra) != -1:
            startindexc = linenum + 3
            #print(startindexc)
        else:
          flagvar = False
        linenum += 1
            
        
      energyline = mylinesb[startindexc]
      energyline = energyline.replace("  | Total energy of the DFT / Hartree-Fock s.c.f. calculation      :","")
      energyline = energyline.replace(" eV","")
      energyline = energyline.replace("     ","")
      energyline = energyline.replace("    ","")        
      
      #print(energyline)
        
      f.writelines("%s\n" % energyline)
        

        
        
      
      
        