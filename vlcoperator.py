#!/usr/bin/env python
# -*- encoding: latin-1 -*-  

# telnet: 127.0.0.1 4212

import subprocess, urllib, time, re

class VLCOperator(object):
    """Controller for VideoLAN Client (VLC)"""
    
    def __init__(self, vlc_command):
        """Initializes the controller"""
        #self.command = '%s --extraintf telnet' % vlc_command
        command = '%s --intf http' % vlc_command
        subprocess.Popen(command, shell=False)
    
    def play(self, mrl):
        """Plays the file/stream/whatever provided by the MRL"""
        pass
    
    def addtoqueue(self, mrl):
        p = urllib.urlopen("http://localhost:8080/?control=add&mrl=%s" % mrl)
        p.close()
    
    def stoptrack(self):
        p = urllib.urlopen("http://localhost:8080/?control=stop")
        p.close()
    
    def starttrack(self):
        """Starts the last track in the queue"""
        # get the queue
        p = urllib.urlopen('http://localhost:8080/')
        result = p.read()
        p.close()
        
        # get the sequence numbers
        rex = re.compile(r'<a href="\?control=play&amp;item=(\d)*?">')
        elements = rex.findall(result)
        
        # start the last track
        p = urllib.urlopen('http://localhost:8080/?control=play&item=%s' % elements[-1])
        p.close()
    
    def shutdown(self):
        try:
            p = urllib.urlopen('http://admin:admin@localhost:8080/admin/?control=shutdown')
            #p.close()
        except AttributeError:
            # silence it
            pass
    
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
    #time.sleep(1)
    vlco.addtoqueue('mms://stream1.orf.at/fm4_live')
    #time.sleep(1)
    vlco.starttrack()
    print 'Waiting'
    time.sleep(20)
    print 'Quitting'
    vlco.shutdown()
    print 'Dying'