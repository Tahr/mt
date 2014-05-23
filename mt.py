
#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
def start():
    print 'Multi Tool'
    print '+-------------------+'
    print '| 1) Calculator     |'
    print '| 2) Text to Binary |'
    print '| 3) Random Number  |'
    print "| 4) OS Detector    |"
    print '| 5) Exit           |'
    print '+-------------------+'
    uic = raw_input('>>>')
    if uic == "1":
        calc()
    if uic == "2":
        ttb()
    if uic == "3":
        rn()
    if uic == "4":
        od()
    else:
        cls()
        print "Invaild Command! Restart? (y/n)"
        ryn = raw_input("(y/n)>>> ")
        if ryn == "y":
            start()
        if ryn == "n":
            cls()
            print "Exiting"
            sys.exit(0)
def calc():
    cls()
    import math
    print '+--------------------------+'
    print '| 1) Addition              |'
    print '| 2) Subtraction           |'
    print '| 3) Multiplacation        |'
    print '| 4) Division              |'
    print '| 5) Square Root *Not done | '
    print '+--------------------------+'
    uc = raw_input('>>> ')
    if uc == '1':
        cls()
        print '| Addition |'
        print 'Number 1:'
        n1 = input('>>> ')
        print 'Number 2:'
        n2 = input('>>> ')
        t = n1 + n2
        print str(n1) + ' + ' + str(n2) + ' = ' + str(t)
        print("Would you like to restart? (y/n)")
        rq = raw_input(">>> ")
        if rq == "y":
            calc()
            cls()
        if rq == "n":
            import sys
            sys.exit(0)
    elif uc == '2':
        cls()
        print '| Subtraction |'
        print 'Number 1:'
        n1 = input('>>> ')
        print 'Number 2:'
        n2 = input('>>> ')
        t = n1 - n2
        print str(n1) + ' + ' + str(n2) + ' = ' + str(t)
        print("Would you like to restart? (y/n)")
        rq = raw_input(">>> ")
        if rq == "y":
            calc()
            cls()
        if rq == "n":
            import sys
            sys.exit(0)
    elif uc == '3':
        cls()
        print '| Multiplacation |'
        print 'Number 1:'
        n1 = input('>>> ')
        print 'Number 2:'
        n2 = input('>>> ')
        t = n1 * n2
        print str(n1) + ' x ' + str(n2) + ' = ' + str(t)
        print("Would you like to restart? (y/n)")
        rq = raw_input(">>> ")
        if rq == "y":
            calc()
            cls()
        if rq == "n":
            import sys
            sys.exit(0)
    elif uc == '4':
        cls()
        print '| Divison |'
        print 'Number 1:'
        n1 = input('>>> ')
        print 'Number 2:'
        n2 = input('>>> ')
        t = n1 / n2
        r = n1 % n2
        print str(n1) + ' / ' + str(n2) + ' = ' + str(t) + ' R ' + str(r)
        print("Would you like to restart? (y/n)")
        rq = raw_input(">>> ")
        if rq == "y":
            calc()
            cls()
        if rq == "n":
            import sys
            sys.exit(0)
def ttb():
    cls()
    import binascii
    print '| Text to Binary |'
    print 'Text: '
    s = raw_input('>>> ')
    b = bin(int(binascii.hexlify(s), 16))
    print 'Converted ' + s + ' to ' + b
    print 'Binary to Text (y/n)'
    btt = raw_input('>>> ')
    if btt == 'y':
        print 'Binary: '
        b = raw_input('>>> ')
        n = int(b, 2)
        bt = binascii.unhexlify('%x' % n)
        print bt
    if btt == 'n':
        print("Would you like to restart? (y/n)")
        rq = raw_input(">>> ")
        if rq == "y":
            calc()
            cls()
        if rq == "n":
            import sys
            sys.exit(0)
def rn():
    cls()
    print '| Random Number |'
    print 'From: '
    f = input('>>> ')
    print 'To: '
    t = input('>>> ')
    from random import randint
    rn = randint(f, t)
    print rn
    print("Would you like to restart? (y/n)")
    rq = raw_input(">>> ")
    if rq == "y":
        calc()
        cls()
    if rq == "n":
        import sys
        sys.exit(0)
def cls():
    import subprocess as sp
    import platform
    osp = platform.system()
    
    if osp == "Windows":
        sp.call('cls',shell=True)
    if osp == "Darwin" or "Linux":
        sp.call('clear',shell=True)

def od():
    cls()
    import subprocess as sp
    import platform
    oso = platform.system()
    osa = platform.machine()
    nn = platform.node()
    if oso == "Darwin":
        print("You are on Mac OS X " + osa + " with computer name " + nn)
    if oso == "Windows":
        print("You are on Windows " + osa + " with computer name " + nn)
    if oso == "Linux":
        print("You are on Linux" + osa + " with computer name " + nn)
    print("Would you like to restart? (y/n)")
    rq = raw_input(">>> ")
    if rq == "y":
        calc()
        cls()
    if rq == "n":
        import sys
        sys.exit(0)

start()
