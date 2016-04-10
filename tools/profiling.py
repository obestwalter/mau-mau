import sys

import os

from mau_mau.stats import winner_distribution

userPath = os.path.expanduser('~')
pmPath = os.path.join(userPath, '.opt/pyvmmonitor/public_api')
print("looking for monitor at '%s'" % (pmPath))
sys.path.append(pmPath)

import pyvmmonitor


@pyvmmonitor.profile_method
def profile_stuff():
    winner_distribution()
