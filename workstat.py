import cli
import os
from assets import *
from locales import _

LOOP = True
FILENUM = 0
SLIST = []


def exec():
    while LOOP == True:
        stamain()

def stamain():
    global LOOP, SLIST
    try:
        ansstr = cli.cmd(_("stat"))
    except KeyboardInterrupt:
        LOOP = False
        return
    SLIST = ansstr.strip().split(" ")
    verb = SLIST[0]
    if verb == "exit":
        LOOP = False
        return
    elif verb == "help":
        print(SHARED["ns"])
        print(gethelp("stat"))
    else:
        if verb != "":
            cli.errorhandler(1, "{0}: {1}".format(verb, SHARED["cnf"]))

if __name__ == "__main__":
    exec()
