#!/usr/bin/env python
# -*- encoding: UTF-8 -*-

import base

class FFHParser(base.StationBase):
    """Parser for Hitradio FFH"""
    
    __station__ = 'FFH'
    
    def __init__(self, url='http://www.ffh.de/api/webradio.php'):
        base.StationBase.__init__(self, url)
    
    def parse(self):
        """Call feed first"""
        artists = self.cut_content('<h5>', '</h5>')
        self.artist = self.capstext(artists[0])
        
        titles = self.cut_content('<h6>', '</h6>')
        self.title = self.capstext(titles[0])
    
    def current_track(self):
        return u"%s - %s" % (self.artist, self.title)

Parser = FFHParser

if __name__ == '__main__':
    base.test_parser(Parser, 'ffh.html')
