'''
Simple Command Line Interface
by Sunnyboy971
Enjoy!
'''
from assets import *

ARGS = "Not Available"
ARG_TOSTDOUT = False
ARG_VERBOSE = True
sym = CLI["sym"][1]


def cmd(prompt: str = "Make", CtrlBehave: str = "", Customstyle: bool = False):
    '''
    Simple command line interface implement.
    '''
    try:
        if Customstyle == True:
            return str(input(prompt))
        else:
            return str(input("[{}] > ".format(prompt)))
    except KeyboardInterrupt:
        print()
        if CtrlBehave == "Loop":
            return cmd(prompt, CtrlBehave)
        elif CtrlBehave == "Empty":
            return ""
        else:
            raise KeyboardInterrupt


def errorhandler(type: int = 3, msg: str = "Testing notification."):
    '''
    Return a notification when needed. For example::

        errorhandler(0, "Fatal error!")

    returns a fatal error indicator and make the script exit with code 1.
    '''
    if type == 4 and ARG_VERBOSE == True:
        print("{0}: {1}".format(sym[type], msg))
    else:
        print("{0}: {1}".format(sym[type], msg))
    if type == 0:
        exit(1)


def argmenu():
    '''
    Return a command line asking for arguments to be added.
    '''
    ans = cmd(CLI["argcmd"][1], "Empty")
    if ans == "?" or ans == None:
        print(ARGS)
        return argmenu()
    arglist = ans.split(" ")
    return arglist


def choices(prompt: str = "Choose:", ch: list = [], default: str = "", AllowMultiple: bool = False):
    if len(ch) == 0:
        errorhandler(2, CLI["nae"][1])
        return []
    if AllowMultiple == True:
        a = "at least one"
    else:
        a = "one"
    for i in range(len(ch)):
        print("[{0}] {1}".format(i+1, ch[i]), end="\t")
    print()
    if default != "":
        print(CLI["default"][1].format(default), end=" ")
    try:
        ans = input(prompt)
    except KeyboardInterrupt:
        errorhandler(0, CLI["kbi"][1])
        exit(1)
    except EOFError:
        errorhandler(0, CLI["eof"][1])
        exit(1)
    prelist = ans.split(" ")
    anslist = []
    if "" in prelist:
        if default != "":
            errorhandler(2, CLI["0ed"][1].format(default))
            return default
        else:
            errorhandler(1, CLI["0e"][1].format(a))
            return choices(prompt, ch, default, AllowMultiple)
    for i in prelist:
        try:
            anslist.append(ch[int(i)-1])
        except ValueError:
            errorhandler(1, CLI["ve"][1])
            return choices(prompt, ch, default, AllowMultiple)
        except IndexError:
            errorhandler(1, CLI["or"][1])
            return choices(prompt, ch, default, AllowMultiple)
    if len(anslist) > 1 and AllowMultiple == False:
        errorhandler(1, CLI["nmc"][1])
        return choices(prompt, ch, default, AllowMultiple)
    return anslist
