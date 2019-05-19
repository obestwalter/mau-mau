import sys

import os

from mau_mau.stats import Stats

userPath = os.path.expanduser("~")
pmPath = os.path.join(userPath, ".opt/pyvmmonitor/public_api")
print(f"looking for monitor at '{pmPath}'")
sys.path.append(pmPath)


import pyvmmonitor


@pyvmmonitor.profile_method
def profile_stuff():
    Stats().winners()
