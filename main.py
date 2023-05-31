# for CLI interface
import cli
# subs to be imported
import replace
import workstat
# some assets & locale support
from assets import *
from locales import _

LOOP = True
ANSSTR = ""

def mainloop():
    global LOOP, ANSSTR
    try: ANSSTR = cli.cmd(_("Mainmenu"))
    except KeyboardInterrupt:
        LOOP = False
        return
    verb = ANSSTR.strip().split(" ")[0]
    if verb == "exit": exit(0)
    elif verb == "about": print(CREDIT)
    elif verb == "help": print(HELP["main"])
    elif verb == "replace": replace.exec()
    elif verb == "stat": workstat.exec()
    else: cli.errorhandler(1, "{0}: {1}".format(verb, SHARED["cnf"]))


if __name__ == "__main__":
    print(CREDIT)
    while LOOP == True: mainloop()
