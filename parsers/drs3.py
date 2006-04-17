#!/usr/bin/env python
# -*- encoding: latin-1 -*-

import base

class DRS3Parser(base.StationBase):
    """DRS3"""
    
    __station__ = 'DRS3'
    __version__ = '0.1.0'
    
    def __init__(self, url='http://www.drs.ch/webradioplayer/r04musicSearchForm.cfm?prg=DRS3'):
        base.StationBase.__init__(self, url)
    
    def parse(self):
        """Call feed first"""
        tracks = self.cut_content('<td class="maintext">', '</td>')
        
        self.artist = self.cut_content('', '<br>', tracks[0])[0]
        self.title = self.cut_content('<b>', '</b>', tracks[0])[0]
    
    def current_track(self):
        return "%s - %s" % (self.capstext(self.artist), self.capstext(self.title))

Parser = DRS3Parser

if __name__ == '__main__':
    base.test_parser(Parser, 'drs3.html')
    