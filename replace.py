import cli
import os
from assets import *
from locales import _

LOOP = True
PRESTR = ""
MODE = _("Simple")
SLIST = []
# This is a file
TARGET = ""
WTARGET = ""
BUFFER = []
SRCSTR = ""
TAGSTR = ""
OUTSTR = ""
TODO = []


def exec():
    while LOOP == True:
        repmain()


def fileio(target: str, typ: str):
    global TARGET, BUFFER, WTARGET
    if typ == "open":
        try:
            TARGET = open(target, "r", encoding="utf8")
            BUFFER = TARGET.read().split("\n")
        except FileNotFoundError:
            cli.errorhandler(1, SHARED["cnf"])
        else:
            cli.errorhandler(3, SHARED["fopened"].format(target))
    elif typ == "close":
        if TARGET == "":
            cli.errorhandler(2, SHARED["faclosed"])
        else:
            TARGET.close()
            cli.errorhandler(3, SHARED["fclosed"].format(TARGET.name))
            TARGET = ""
    elif typ == "write":
        if TARGET == "" and target == "":
            cli.errorhandler(2, SHARED["faclosed"])
        else:
            try:
                if target == "":
                    TARGET.close()
                    WTARGET = open(TARGET.name, "x", encoding="utf8")
                else:
                    WTARGET = open(target, "x", encoding="utf8")
            except FileExistsError:
                cli.errorhandler(2, SHARED["overwrite"])
                try:
                    os.remove(target)
                except PermissionError:
                    cli.errorhandler(1, SHARED["permission"])
                    return
                WTARGET = open(target, "x", encoding="utf8")
            for i in BUFFER:
                WTARGET.write(i + "\n")
            cli.errorhandler(3, SHARED["sfinished"].format(WTARGET.name))
            WTARGET.close()
            # This line still has problems. Have the need to open TARGET? <TODO>
            # if TARGET != "": TARGET = open(TARGET.name, "r", encoding="utf8")

    return


def mkcmd():
    global PRESTR, SRCSTR, TAGSTR, TODO
    if SRCSTR == "" and TAGSTR == "":
        PRESTR = ""
    elif SRCSTR == "":
        PRESTR = " \033[5;33m?\033[0m -> \"\033[1;36m{}\033[0m\"".format(
            TAGSTR)
    elif TAGSTR == "":
        PRESTR = " \"\033[1;36m{}\033[0m\" -> \"\"".format(SRCSTR)
    else:
        PRESTR = " \"\033[1;36m{0}\033[0m\" -> \"\033[1;36m{1}\033[0m\"".format(
            SRCSTR, TAGSTR)
    if len(TODO) != 0:
        PRESTR += " \033[1;36m*\033[0m"


def mtodo():
    global TODO, SLIST, SRCSTR, TAGSTR, MODE
    if len(SLIST) == 0:
        cli.errorhandler(1, SHARED["argn"].format("todo"))
        return
    verbt = SLIST[0]
    if verbt == "add":
        TODO.append([len(TODO) + 1, MODE, SRCSTR, TAGSTR])
        SRCSTR = TAGSTR = ""
    if verbt == "list":
        if len(TODO) == 0:
            cli.errorhandler(3, REPLACE["ntodo"])
        else:
            print(SHARED["total"].format(len(TODO)))
            for i in TODO:
                print("[{0} {1}] \"{2}\" -> \"{3}\"".format(i[0], i[1], i[2], i[3]))
    if verbt == "exec":
        while len(TODO) != 0:
            doreplace(TODO[0][1], TODO[0][2], TODO[0][3])
            TODO.pop(0)
    return


def doreplace(typ: str, src: str, tag: str):
    global BUFFER
    cli.errorhandler(3, REPLACE["doing"].format(typ, src, tag))
    if typ == REPLACE["modelist"][0]:
        # Simple mode
        for i in range(len(BUFFER)):
            BUFFER[i] = BUFFER[i].replace(src, tag)
    elif typ == REPLACE["modelist"][1]:
        # Advanced mode
        s = src.partition("{*}")
        t = tag.partition("{*}")
        sa = s.index("{*}")
        ta = t.index("{*}")
        if (s[2] == "" and s[1] == "") or (t[2] == "" and t[1] == ""):
            cli.errorhandler(2, REPLACE["rerror"].format(src))
            return
        else:
            # Multiple *s not supported yet <TODO>
            for i in range(len(BUFFER)):
                loc1 = loc2 = 0
                tmp = ""
                ss = tt = ""
                if sa == 0:
                    loc2 = BUFFER[i].find(s[1])
                    if loc2 == -1: return
                    tmp = BUFFER[i][0:loc2]
                    ss = BUFFER[i][0:loc2+len(s[2])+1]
                else:
                    try:
                        s.index("")
                    except ValueError:
                        loc1 = BUFFER[i].find(s[0])
                        loc2 = BUFFER[i].find(s[2])
                        if loc2 == -1 or loc1 == -1: return
                        tmp = BUFFER[i][loc1+len(s[0]):loc2]
                        ss = BUFFER[i][loc1:loc2+len(s[2])+1]
                    else:
                        loc1 = BUFFER[i].find(s[0])
                        if loc1 == -1: return
                        tmp = BUFFER[i][-(loc1+len(s[0]))]
                        ss = BUFFER[i][-(loc1-len(s[0]))]
                if ta == 0:
                    tt = tmp + t[1]
                else:
                    try:
                        s.index("")
                    except ValueError:
                        tt = t[0] + tmp + t[2]
                    else:
                        BUFFER[i] = BUFFER[i].replace(s[2],"")
                        tt = t[0] + tmp
                # "What is {*}?" -> "{*} 是什么？"
                BUFFER[i] = BUFFER[i].replace(ss, tt)
    elif typ == REPLACE["modelist"][2]:
        pass
    pass


def preview():
    global BUFFER
    for i in BUFFER:
        print(i)
    return


def mode():
    global MODE
    MODE = cli.choices(_("Select a mode:"), REPLACE["modelist"])[0]


def repmain():
    global LOOP, SRCSTR, TAGSTR, PRESTR, OUTSTR, MODE, SLIST
    target = ""
    mkcmd()
    try:
        ansstr = cli.cmd("\033[1;36m{0}\033[0m".format(
            MODE) + _("replace") + PRESTR)
    except KeyboardInterrupt:
        LOOP = False
        return
    SLIST = ansstr.strip().split(" ")
    verb = SLIST[0]
    if verb == "exit":
        LOOP = False
        return
    elif verb == "help":
        print(HELP["replace"])
    elif verb == "todo":
        SLIST.pop(0)
        mtodo()
    elif verb == "open":
        if len(SLIST) == 1:
            target = cli.cmd(SHARED["target"], "Empty")
        else:
            target = SLIST[1]
        fileio(target, "open")

    elif verb == "close":
        fileio("", "close")

    elif verb == "source":
        if len(SLIST) == 1:
            SRCSTR = cli.cmd(REPLACE["source"], "Default", Default=SRCSTR)
        else:
            SLIST.pop(0)
            SRCSTR = SLIST.pop(0)
            for i in SLIST:
                SRCSTR += " " + i
    elif verb == "target":
        if len(SLIST) == 1:
            TAGSTR = cli.cmd(REPLACE["target"], "Default", Default=TAGSTR)
        else:
            SLIST.pop(0)
            TAGSTR = SLIST.pop(0)
            for i in SLIST:
                TAGSTR += " " + i
    elif verb == "mode":
        if len(SLIST) == 1:
            mode()
        else:
            try:
                MODE = REPLACE["modelist"][int(SLIST[1])]
            except (TypeError, ValueError, IndexError):
                cli.errorhandler(1, SHARED["invalid"])
    elif verb == "save":
        ans = cli.choices(SHARED["aoverwrite"],
                          SHARED["yesno"], SHARED["yesno"][0])
        if ans == SHARED["yesno"][1]:
            fileio("", "write")
    elif verb == "saveas":
        if len(SLIST) == 1:
            OUTSTR = cli.cmd(SHARED["target"], "Empty")
            OUTSTR = OUTSTR.split(" ")
            for i in OUTSTR:
                fileio(i, "write")
        else:
            SLIST.pop(0)
            OUTSTR = SLIST
            for i in OUTSTR:
                fileio(i, "write")
    elif verb == "preview":
        preview()
    else:
        if verb != "":
            cli.errorhandler(1, "{0}: {1}".format(verb, SHARED["cnf"]))


if __name__ == "__main__":
    exec()
