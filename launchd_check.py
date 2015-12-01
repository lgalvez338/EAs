#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Naively checks against a manually self-maintained whitelist"""


import os
import json
import subprocess
import sys


def osquery_check():
    """bail early if osquery not installed"""
    if not os.path.exists('/usr/local/bin/osqueryi'):
        result = 'wha? no osquery? bro, do you even lift?'
        print "<result>%s</result>" % result
        sys.exit(0)

def run_osquery(sql):
    """take sql command you'd like json output for from osquery"""
    cmd = ['/usr/local/bin/osqueryi', '--json', sql]
    jsony_out = subprocess.check_output(cmd)
    try:
        jsony_dictlist = json.loads(jsony_out)
    except ValueError:
        sys.exit(1)
    return jsony_dictlist

def main():
    """gimme some main"""
    osquery_check()

    # LaunchA list, includes users home folder
    d_s_allowed = ['com.adobe.AAM.Updater-1.0.plist',
                   'com.adobe.AdobeCreativeCloud.plist',
                   #pylint: disable=line-too-long
                   'com.adobe.ARM.202f4087f2bbde52e3ac2df389f53a4f123223c9cc56a8fd83a6f7ae.plist',#Reader
                   'com.adobe.ARM.de23d1e3aa2d00ce38d73f10fcbdc8dcaaaf6be989610710a1ddda77.plist',#Acrobat XI pro
                   'com.adobe.ARM.df0ab5bbe6f698196fcc21e3c1e66dcb758bd911f4d637272d9d8109.plist',#Acrobat X
                   'com.airwatch.mac.agent.plist',
                   'com.apple.FolderActions.folders.plist',#may be empty WatchPatchs array, probably safe to delete if so
                   'com.avast.home.userinit.plist',
                   'com.barco.clicksharelauncher.plist',
                   'com.bombich.ccc-user-agent.plist',
                   'com.cisco.anyconnect.gui.plist',
                   'com.citrix.AuthManager_Mac.plist',
                   'com.citrix.DesktopPlayer.plist',
                   'com.citrix.ReceiverHelper.plist',
                   'com.citrix.ServiceRecords.plist',
                   'com.citrixonline.GoToMeeting.G2MUpdate.plist',
                   'com.citrixonline.GoToMyPC.LaunchAgent.plist',
                   'com.deploystudio.FinalizeApp.plist',
                   'com.deploystudio.finalizeScript.plist',
                   'com.github.outset.login.plist',
                   'com.google.keystone.agent.plist',
                   'com.googlecode.munki.ManagedSoftwareCenter.plist',
                   'com.googlecode.munki.ManagedSoftwareUpdate.plist',
                   'com.googlecode.munki.MunkiStatus.plist',
                   'com.googlecode.munki.MunkiStatusLogout.plist',
                   'com.googlecode.munki.managedsoftwareupdate-loginwindow.plist',
                   'com.google.santagui.plist',
                   'com.jamfsoftware.jamf.agent.plist',
                   'com.leapmotion.Leap-Motion.plist',
                   'com.Logitech.Control Center.Daemon.plist',
                   'com.microsoft.LaunchAgent.SyncServicesAgent.plist',
                   'com.oracle.java.Java-Updater.plist',
                   'com.rim.BBLaunchAgent.plist',
                   'com.rim.blackberrylink.BlackBerry-Link-Helper-Agent.plist',
                   'com.rim.PeerManager.plist',
                   'com.seagate.dashboard.plist',
                   'com.spotify.webhelper.plist',
                   'com.teamviewer.teamviewer.plist',
                   'com.teamviewer.teamviewer_desktop.plist',
                   # 'net.optimum.iptv.optimumapp.agent.v3.plist',# see prog args - omgwtfbbq
                   # 'opt.plist',#seriously, optimum online? ಠ_ಠ
                   'org.macosforge.xquartz.startx.plist',
                   'org.montefiore.AutoDMGd-LadminPrefs.plist',
                   'org.montefiore.scriptrunner.plist',
                   'org.virtualbox.vboxwebsrv.plist',
                   'Safe.Connect.client.plist']
    # /Library/LaunchDaemons contents allowed, apends
    d_s_allowed += ['com.adobe.adobeupdatedaemon.plist',
                    'com.adobe.agsservice.plist',
                    'com.adobe.ARM.SMJobBlessHelper.plist',
                    'com.adobe.fpsaud.plist',
                    'com.adobe.SwitchBoard.plist',
                    'com.airwatch.airwatchd.plist',
                    'com.airwatch.awcmd.plist',
                    'com.apple.aelwriter.plist',
                    'com.apple.SoftwareUpdate.mtversionlog.plist',
                    'com.apple.spirecorder.plist',
                    'com.attotech.iscsid.plist',
                    #pylint: disable=line-too-long
                    'com.barebones.authd.plist',# https://groups.google.com/forum/#!topic/bbedit/8vPQCmeN7aQ
                    'com.bombich.ccc.plist',
                    'com.bombich.ccchelper.plist',
                    'com.cisco.anyconnect.ciscod.plist',
                    'com.cisco.anyconnect.vpnagentd.plist',
                    'com.citrix.agadminservice.plist',
                    'com.citrixonline.GoToMyPC.CommAgent.plist',
                    'com.crashplan.engine.plist',
                    'com.datarobotics.ddservice64d.plist',
                    'com.deploystudio.finalizeCleanup.plist',
                    'com.deploystudio.server.plist',
                    'com.deterministicnetworks.daemon.dniregsvr.plist',
                    'com.facebook.osqueryd.plist',
                    'com.fernlightning.fseventer.plist',
                    'com.fitbit.galileod.plist',
                    'com.github.autopkg.autopkginstalld.plist',
                    'com.github.autopkg.autopkgserver.plist',
                    'com.github.GitHub.GHInstallCLI.plist',
                    'com.github.outset.boot.plist',
                    'com.google.keystone.daemon.plist',
                    'com.googlecode.munki.logouthelper.plist',
                    'com.googlecode.munki.managedsoftwareupdate-check.plist',
                    'com.googlecode.munki.managedsoftwareupdate-install.plist',
                    'com.googlecode.munki.managedsoftwareupdate-manualcheck.plist',
                    'com.google.santad.plist',
                    'com.grahamgilbert.crypt.needsescrow.plist',
                    'com.jamfsoftware.jamf.daemon.plist',
                    'com.jamfsoftware.startupItem.plist',
                    'com.jamfsoftware.task.checkForTasks.plist',
                    'com.jamfsoftware.task.1.plist',
                    'com.leapmotion.leapd.plist',# ಠ_ಠ
                    'com.logmein.join.me.update-helper.plist',
                    'com.macromates.auth_server.plist',
                    'com.makerbot.conveyor.plist',
                    'com.microsoft.office.licensing.helper.plist',
                    'com.oracle.java.Helper-Tool.plist',
                    'com.oracle.java.JavaUpdateHelper.plist',
                    'com.promise.bgasched.plist',
                    'com.promise.BGPMain_R.plist',
                    'com.promise.emaild.plist',
                    'com.puppetlabs.mcollective.plist',
                    'com.puppetlabs.pe-puppet.plist',
                    'com.puppetlabs.pe-mcollective.plist',
                    'com.puppetlabs.puppet.plist',
                    #'com.rim.BBDaemon.plist', what year is it?
                    #'com.rim.nkehelper.plist',
                    #'com.rim.tunmgr.plist',
                    'com.skype.skypeinstaller.plist',
                    'com.symantec.manufacturer.agent.plist',
                    'com.teamviewer.Helper.plist',
                    'com.teamviewer.teamviewer_service.plist',
                    'com.tunnelbear.mac.tbeard.plist',
                    'com.VTechLLNService.plist',
                    'com.zabbix.zabbix_agentd.plist',
                    'fr.whitebox.packages_dispatcher.plist',
                    'org.macosforge.xquartz.privileged_startx.plist',
                    'org.montefiore.LocalMCX-setup.plist',
                    'org.virtualbox.startup.plist',
                    'org.wireshark.ChmodBPF.plist',
                    'Safe.Connect.plist']
    # /System/Library/LaunchDaemons and Agents appended
    d_s_allowed += ['bootps.plist',
                    'com.seagate.TBDecorator.plist',# ಠ_ಠ
                    'com.vix.cron.plist',
                    'exec.plist',
                    'finger.plist',
                    'ftp.plist',
                    'login.plist',
                    'ntalk.plist',
                    'org.apache.httpd.plist',
                    'org.cups.cups-lpd.plist',
                    'org.cups.cupsd.plist',
                    'org.net-snmp.snmpd.plist',
                    'org.ntp.ntpd.plist',
                    'org.openldap.slapd.plist',
                    'org.postfix.master.plist',
                    'org.postfix.newaliases.plist',
                    'shell.plist',
                    'ssh.plist',
                    'telnet.plist',
                    'tftp.plist',
                    'org.openbsd.ssh-agent.plist',]# The only system launchagent

    launchd_dicts = run_osquery('select name, path from launchd')
    to_investigate = []
    for each in launchd_dicts:
        if each['name'].startswith("com.apple"):
            pass
        elif each['name'].startswith("com.bombich.ccc.scheduledtask"):
            pass
        else:
            if each['name'] not in d_s_allowed:
                to_investigate.append(each['path'])

    if to_investigate:
        result = "Launchd not in allowed, investigate:\n" + "\n".join(*[to_investigate])
    else:
        result = "No out-of-ordinary launchd's installed."

    print "<result>%s</result>" % result

if __name__ == '__main__':
    main()
