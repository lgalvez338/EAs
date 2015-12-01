#!/usr/bin/python
import subprocess
import plistlib

CAUGHT_USERS = ''

excludes = ["jssadmin", "montyadm", "localmontyadm", "root", "iosadmin", "macadmin"]
p = subprocess.Popen(['dscl', '-plist', '.', '-read', '/Groups/admin', 'dsAttrTypeStandard:GroupMembership'],
    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
(stdout_data, err) = p.communicate()
plist = plistlib.readPlistFromString(stdout_data)

user_list = plist.get('dsAttrTypeStandard:GroupMembership')

for usr in user_list:
     if usr not in excludes:
         CAUGHT_USERS += "Admin user %s not in allowed list\n" % usr

if not CAUGHT_USERS == '':
    print('<result>' + CAUGHT_USERS + '</result>')
else:
    print('<result>None</result>')
