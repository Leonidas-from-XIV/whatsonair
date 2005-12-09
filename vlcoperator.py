#!/usr/bin/env python
# -*- encoding: latin-1 -*-  

# telnet: 127.0.0.1 4212

import subprocess, telnetlib

class VLCOperator(object):
    def __init__(self, vlc_command):
        self.command = '%s --extraintf telnet' % vlc_command
        self.vlc_running = False
    
    def play(self, mrl):
        # first quit vlc if it is already running
        if self.vlc_running:
            self.shutdown()

        self.proc = subprocess.Popen('%s play %s' % (self.command, mrl),
            shell=False)
        # register vlc as running
        self.vlc_running = True
    
    def shutdown(self):
        """Shuts down VLC"""
        # connect
        self.conn = telnetlib.Telnet('127.0.0.1', 4212)
        # login
        self.conn.write('admin\n')
        # close
        self.conn.write('shutdown\n')
        # register
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
    import time
    executable = discover_executable()
    vlco = VLCOperator(executable)
    
    vlco.play('rtsp://213.254.238.73:554/real.amazon-de.eu2/phononet/B/0/0/0/0/6/L/7/X/Q/01.02.rm?cloakport=80,554,7070')
    #vlco.play('file://C:/hell.mp3')
    print 'Waiting'
    time.sleep(10)
    print 'Quitting'
    vlco.shutdown()
    print 'Dying'



