import cli
import os
from assets import *
from locales import _

LOOP = True
ANSSTR = ""


def exec():
    while LOOP == True:
        repmain()


def wizard():
    a = cli.choices(_("Select a mode:"), REPLACE["modelist"][1])


def repmain():
    global LOOP, ANSSTR
    try:
        ANSSTR = cli.cmd(REPLACE["title"][1])
    except KeyboardInterrupt:
        LOOP = False
        return
    verb = ANSSTR.strip().split(" ")[0]
    if verb == "exit":
        LOOP = False
        return
    elif verb == "help":
        print(HELP["replace"])
    elif verb == "wizard":
        wizard()
    else: cli.errorhandler(1, "{0}: {1}".format(verb, SHARED["cnf"][1]))

# opt = cli.cmd(SHARED["target"][1])
# tf = open(opt, "r", encoding="utf8")
# ans = cli.choices("")
# src = cli.cmd(REPLACE["source"][1])
# tga = cli.cmd(REPLACE["target"][1])
#
# tf.close()
#
