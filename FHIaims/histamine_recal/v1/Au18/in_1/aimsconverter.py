import re
import sys
f = open("geometry.in", "w")
g = open("control.in", "w")

#n = len(sys.argv)

nmolecule = 16
nelectrodeL = 18
nLrelax = 4
nelectrodeR = 18
nRrelax = 4
InorOut = "In"

#nmolecule = int(sys.argv[1])
#nelectrodeL = int(sys.argv[2])
#nLrelax = int(sys.argv[3])
#nelectrodeR = int(sys.argv[4])
#nRrelax = int(sys.argv[5])
#InorOut = sys.argv[6]

stepsize = float(0.05)
n_a = int(nmolecule + nelectrodeL)
n_b = int(nmolecule - 1)
n_c = int(nmolecule + nelectrodeL - 1)
n_d = int(nmolecule)
n_e = int(nmolecule + nLrelax - 1)
n_f = int(nmolecule + nelectrodeL + nRrelax - 1)
n_g = int(n_a - 3)
inoutvar = 0
testin = "In"
testout = "Out"
myxyzdata = []
mylines = []
mylinesb = []
mydata = []
mydatab = []
myseconddata = []
moveddata = []
titleline = []
linenum=0
startindex = 0
endindex = 0
itemnum = 0
ErrorFlag = False

if ( InorOut.find(testin) == -1  and InorOut.find(testout) == -1):
    quit()
if InorOut.find(testin) == -1:
    inoutvar = 2            # inoutvar = 2 if electrodes are moving out
else:
    inoutvar = 1            # inoutvar = 1 if electrodes are moving in
    
    

with open ("geometry.in.next_step", "rt") as myfile:
    for myline in myfile:
        linenum += 1
        mylines.append(myline.rstrip('\n'))
        substra = "# What follows is the current estimated Hessian matrix constructed by the BFGS algorithm."
        #print(myline)
        #linenum = len(myfile)-1
        if myline.find(substra) != -1:
            endindex = linenum-1
            #print(startindex)
        else:
            continue
    linenum = 0
    startindex = 4
    for myline in mylines:
        linenum += 1
        if (linenum > startindex and linenum < endindex):
            mydata.append(myline)
        else:
            continue
    
    

    for item in mydata:
        f.writelines("%s\n" % item)
    f.close()
    
    linenum = 0
    with open ("controltemp.in", "rt") as myfileb:
        for mylineb in myfileb:
            linenum += 1
            mylinesb.append(mylineb.rstrip('\n'))
            substra = "#  KS_method	     lapack_fast"
            substrb = "  relax_geometry   bfgs 1.e-2"
            substrc = "#   output aitranss"
            if mylineb.find(substra) != -1:
                KSindex = linenum
                print(KSindex)
            elif mylineb.find(substrb) != -1:
                relaxindex = linenum
                print(relaxindex)
            elif mylineb.find(substrc) != -1: 
                aitranssindex = linenum
                print(aitranssindex)
            else:
                continue
        linenum = 0
        
        for mylineb in mylinesb:
            linenum += 1
            #print(mylineb)
            if (linenum == KSindex):
                mydatab.append("  KS_method	     lapack_fast")
            elif (linenum == relaxindex):
                mydatab.append("#  relax_geometry   bfgs 1.e-2")
            elif (linenum == aitranssindex):
                mydatab.append("   output aitranss")
            else:
                mydatab.append(mylineb)
        
        for item in mydatab:
            g.writelines("%s\n" % item)
        g.close()    


