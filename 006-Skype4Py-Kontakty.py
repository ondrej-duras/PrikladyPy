#!/usr/bin/env python2

# https://pypi.python.org/pypi/Skype4Py/
# set https_proxy=http://proxy.bbn.hp.com:8080
# pip install Sype4Py


import Skype4Py

# Create an instance of the Skype class.
skype = Skype4Py.Skype()

# Connect the Skype object to the Skype client.
skype.Attach()

# Obtain some information from the client and print it out.
print 'Your full name:', skype.CurrentUser.FullName
print 'Your contacts:'
for user in skype.Friends:
    print '    ', user.FullName

