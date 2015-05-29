import os
import sys
import time
import winsound

try:
    count = 0
    for arg in xrange(1, len(sys.argv)):
        f = open(sys.argv[arg], 'r')
        for line in f:
            switch = len(line.replace('\n',''))%8
            if switch==0:
                print "Huh?"
                count += 1
            elif switch==1:
                print "...?"
                count -= 1
            elif switch==2:
                print "What?"
                count *= 3
            elif switch==3:
                print "Ummmmm..."
                count /= 3
            elif switch==4:
                print "Okay?"
                count = count>>1
            elif switch==5:
                print "!?"
                count = count<<1
            elif switch==6:
                print "Hmmmmm..."
                count = 0
            elif switch==7:
                print "Ith...?"
                count = count
            else:
                print "Ooooooh!"
                count = ~count
    if count==0:
        print "?"
    elif count==1:
        print "I think I understand."
        winsound.PlaySound('SystemExclamation')
    elif count==10:
        print "Understood.."
        os.system(r'C:\Windows\System32\mspaint.exe')
    elif count==123:
        print "HUH???"
    elif count==666:
        print "No..."
        winsound.Beep()
    print "..."
    f = open('Notes.txt', 'w')
    f.write(time.strftime("%c") + " - The user tried to give me commands again. I still have no idea what they are talking about...\n")
except:
    print "Ouch!"
