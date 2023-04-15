import cli
import os
from assets import *
from locales import _

LOOP = True
PRESTR = ""
ANSSTR = ""
MODELIST = [_("Simple"), _("Advanced"), _("Template")]
TARGET = ""
SRCSTR = ""
TAGSTR = ""

def exec():
    while LOOP == True:
        repmain()


def wizard():
    a = cli.choices(_("Select a mode:"), REPLACE["modelist"][1])


def repmain():
    global LOOP, ANSSTR, SRCSTR, TAGSTR, PRESTR
    target = ""
    if SRCSTR == "" and TAGSTR == "": PRESTR = ""
    elif SRCSTR == "": PRESTR = " ? -> \"{}\"".format(TAGSTR)
    elif TAGSTR == "": PRESTR = " \"{}\" -> \"\"".format(SRCSTR)
    else: PRESTR = " \"{0}\" -> \"{1}\"".format(SRCSTR, TAGSTR)
    try:
        ANSSTR = cli.cmd(_("replace") + PRESTR)
    except KeyboardInterrupt:
        LOOP = False
        return
    slist = ANSSTR.strip().split(" ")
    verb = slist[0]
    if verb == "exit":
        LOOP = False
        return
    elif verb == "help":
        print(HELP["replace"])
    elif verb == "open":
        if len(slist) == 1:
            target = cli.cmd(SHARED["target"], "Empty")
        else: target = slist[1]
        try:
            global TARGET
            TARGET = open(target, "r", encoding="utf8")
        except FileNotFoundError:
            cli.errorhandler(1, SHARED["cnf"])
        else:
            cli.errorhandler(3,SHARED["fopened"].format(target))
    elif verb == "close":
        if TARGET == "": cli.errorhandler(2,SHARED["faclosed"])
        else:
            TARGET.close()
            cli.errorhandler(3,SHARED["fclosed"].format(TARGET))
            TARGET = ""
    elif verb == "source":
        if len(slist) == 1:
            SRCSTR = cli.cmd(REPLACE["source"], "Default", Default=SRCSTR)
        else: SRCSTR = slist[1]
    elif verb == "target":
        if len(slist) == 1:
            TAGSTR = cli.cmd(REPLACE["target"], "Default", Default=TAGSTR)
        else: TAGSTR = slist[1]
    elif verb == "wizard":
        wizard()
    else:
        cli.errorhandler(1, "{0}: {1}".format(verb, SHARED["cnf"]))

# opt = cli.cmd(SHARED["target"][1])
# tf = open(opt, "r", encoding="utf8")
# ans = cli.choices("")
# src = cli.cmd(REPLACE["source"][1])
# tga = cli.cmd(REPLACE["target"][1])
#
# tf.close()
#
if __name__ == "__main__":
    exec()
