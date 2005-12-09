#!/usr/bin/env python
# -*- encoding: latin-1 -*-  

# telnet: 127.0.0.1 4212

import subprocess, telnetlib

class VLCOperator(object):
    """Controller for VideoLAN Client (VLC)"""
    
    def __init__(self, vlc_command):
        """Initializes the controller"""
        #self.command = '%s --extraintf telnet' % vlc_command
        self.command = '%s -I telnet' % vlc_command
        self.vlc_running = False
    
    def play(self, mrl):
        """Plays the file/stream/whatever provided by the MRL"""
        # first quit vlc if it is already running
        if self.vlc_running:
            self.shutdown()
        
        # start vlc
        self.proc = subprocess.Popen('%s play %s' % (self.command, mrl),
            shell=False)
            
        # register vlc as running
        self.vlc_running = True
    
    def shutdown(self):
        """Shuts down VLC"""
        # connect to vlc
        self.conn = telnetlib.Telnet('127.0.0.1', 4212)
        # login as admin
        self.conn.write('admin\n')
        # tell vlc to quit
        self.conn.write('shutdown\n')
        # register vlc as stopped
        self.vlc_running = False
    
def discover_executable():
    """Searches the VideoLAN CLient executable"""
    try:
        import _winreg
        uninstall_key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,
            r'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\VLC media player')
        location = _winreg.QueryValueEx(uninstall_key, 'DisplayIcon')[0]
    except ImportError, e:
        # a non Windows-OS, much easier
        location = 'vlc'
    
    return location

if __name__ == '__main__':
    vlco = VLCOperator(discover_executable())
    
    print 'Opening'
    vlco.play('mms://stream1.orf.at/fm4_live')
    print 'Waiting'
    import time
    time.sleep(20)
    print 'Quitting'
    vlco.shutdown()
    print 'Dying'
