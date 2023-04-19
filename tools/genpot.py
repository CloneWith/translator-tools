import os
fn = "assets.py cli.py main.py replace.py"
loc = str(input("The python installation directory: "))
os.system("python \"{0}\\Tools\\i18n\\pygettext.py\" resource.pot {1}".format(loc, fn))
