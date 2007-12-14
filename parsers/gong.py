#!/usr/bin/env python
# -*- encoding: UTF-8 -*-

import base, urllib

class GongParser(base.StationBase):
    """The parser for Gong"""
    
    __station__ = 'Gong'
    __version__ = '0.9.3'
    
    def __init__(self, url='http://www.radiogong.de/gongphp/header.php'):
        base.StationBase.__init__(self, url)
    
    def parse(self):
        """Call feed first"""
        track = self.cut_content_simple('%2C+', '+%2A')[0]
        artist, title = track.split('%2C+')

        self.artist = self.capstext(urllib.unquote_plus(artist))
        self.title = urllib.unquote_plus(title)
    
    def current_track(self):
        return u"%s - %s" % (self.artist, self.title)

Parser = GongParser

if __name__ == '__main__':
    base.test_parser(Parser, 'justone.html')
    
