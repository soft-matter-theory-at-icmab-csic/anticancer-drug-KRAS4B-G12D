import math
f1 = open('cos1-last500ns-1-radians.dat', 'w')
f2 = open('cos1-last500ns-2-degrees.dat', 'w')
f3 = open('cos1-last500ns.dat', 'r')
for line in f3:
    line = line.strip()
    colunms = line.split()
    x = float(colunms[0])
    y = float(colunms[1])
    y1 =math.acos(y)
    y2 =math.degrees(y1)
    f1.write(str(x) + '\t' + str(y1) + '\n')
    f2.write(str(x) + '\t' + str(y2) + '\n')

f1.close()
f2.close()
f3.close()
