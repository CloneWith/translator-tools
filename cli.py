'''
Simple Command Line Interface
by Sunnyboy971
Enjoy!
'''
from assets import *
from locales import _

ARGS = "Not Available"
ARG_TOSTDOUT = False
ARG_VERBOSE = True
SYM = [_("Fatal"), _("Error"), _("Warning"), _("Info"), _("Detail")]


def cmd(prompt: str = "Make", CtrlBehave: str = "", Customstyle: bool = False, Default: str = ""):
    '''
    Simple command line interface implement.
    '''
    try:
        if Customstyle == True:
            return str(input(prompt))
        else:
            if Default != "": prompt = _("Default:{}").format(Default) + " " + prompt
            return str(input("[{}] > ".format(prompt)))
    except KeyboardInterrupt:
        print()
        if CtrlBehave == "Loop":
            return cmd(prompt, CtrlBehave)
        elif CtrlBehave == "Empty":
            return ""
        elif CtrlBehave == "Def":
            return Default
        else:
            raise KeyboardInterrupt


def errorhandler(type: int = 3, msg: str = "Testing notification."):
    '''
    Return a notification when needed. For example::

        errorhandler(0, "Fatal error!")

    returns a fatal error indicator and make the script exit with code 1.
    '''
    if type == 4 and ARG_VERBOSE == True:
        print("{0}: {1}".format(SYM[type], msg))
    else:
        print("{0}: {1}".format(SYM[type], msg))
    if type == 0:
        exit(1)


def argmenu():
    '''
    Return a command line asking for arguments to be added.
    '''
    ans = cmd(_("Args: [? for help]"), "Empty")
    if ans == "?" or ans == None:
        print(ARGS)
        return argmenu()
    arglist = ans.split(" ")
    return arglist


def choices(prompt: str = "Choose:", ch: list = [], default: str = "", AllowMultiple: bool = False):
    if len(ch) == 0:
        errorhandler(2, _("Alternatives not found."))
        return []
    if AllowMultiple == True:
        a = _("at least one")
    else:
        a = _("one")
    for i in range(len(ch)):
        print("[{0}] {1}".format(i+1, ch[i]), end="\t")
    print()
    if default != "":
        print(_("Default:{}").format(default), end=" ")
    try:
        ans = input(prompt)
    except KeyboardInterrupt:
        errorhandler(0, _("User cancelled the process."))
        exit(1)
    except EOFError:
        errorhandler(0, _("EOF received! Exiting..."))
        exit(1)
    prelist = ans.split(" ")
    anslist = []
    if "" in prelist:
        if default != "":
            errorhandler(2, _("Using default: ").format(default))
            return default
        else:
            errorhandler(1, _("You must choose {} from the list.").format(a))
            return choices(prompt, ch, default, AllowMultiple)
    for i in prelist:
        try:
            anslist.append(ch[int(i)-1])
        except ValueError:
            errorhandler(1, _("Answer with integers please."))
            return choices(prompt, ch, default, AllowMultiple)
        except IndexError:
            errorhandler(1, _("Choice out of range."))
            return choices(prompt, ch, default, AllowMultiple)
    if len(anslist) > 1 and AllowMultiple == False:
        errorhandler(1, _("Multiple choices aren't allowed."))
        return choices(prompt, ch, default, AllowMultiple)
    return anslist
