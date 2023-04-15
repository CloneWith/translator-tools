# Python Localization Sample
import os, gettext, sys

# Support localization
_ = None
def getUserLanguage():
    if (len(sys.argv) > 1):
        return sys.argv[1]
    return "zh-CN"

# Get loc string by language
def getLocStrings():
    currentDir = os.path.dirname(os.path.realpath(__file__))
    return gettext.translation('resources', currentDir, [getUserLanguage(), "en-US"]).gettext

_ = print()
# print(_("Hello"))
