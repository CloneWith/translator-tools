from locales import _

VER = "0.0.1 20230414"

CREDIT = '''
=*= Translator Tools =*=
Made by @Sunnyboy971(https://github.com/Sunnyboy971)
'''

CLI = {
    "na": ["Not Available", "内容暂时不可用。"],
}

SHARED = {
    "target": _("Target file:"),
    "cnf": _("Command not found."),
    "unknownerror": _("An unknown error just occurred. Please report the problem at your convience on Github."),
    "choice": _("Selection:"),
    "fopened": _("File opened: {}"),
    "fclosed": _("File closed: {}"),
    "faclosed": _("No opened file found.")
}

REPLACE = {
    "title": "Replace",
    "source": "String to be replaced:",
    "target": "Replace to:",
    "replaceall": "Replace all occurences in the file?"
}

HELP = {
    "main": _("""
    Available commands:
    help: Display this help message.
    exit: Exit the program.
    about: Show author of the program.
    replace: Enter replace mode.
    [Tip: In the command line, you can go back using ^C.]
    """),
    "replace": _("""
    Available commands in replace mode:
    help: Display this help message.
    exit: Go back to the main menu.
    wizard: Go through the wizard to do what you want to do.
    open: Open the specific file.
    close: Close opened files.
    mode: Choose the replace mode. Available: simple, advanced, template.
    source: Specify the string to be replaced.
    target: Specift the string to be replaced with the source string.
    preview: Preview the changes.
    reveal: Cancel all the changes.
    save: Write changes to the opened file.
    saveas: Write changes to another file specified.
    """)
}
