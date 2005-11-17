#!/usr/bin/env python
# -*- encoding: latin-1 -*-

import base

class JumpParser(base.StationBase):
    """Parser for Jump Radio"""
    
    __station__ = 'Jump'
    __version__ = '0.0.1'
    
    def __init__(self, url='http://www.jumpradio.de/navi/onair.xml'):
        base.StationBase.__init__(self, url)
    
    def parse(self):
        """Parses the XML-files provided by the radio station"""
        # first, cut out the artist (escape the CDATA parts)
        self.artist = self.cut_content('<interpret><![CDATA[', ']')[0]
        self.title = self.cut_content('<titel><![CDATA[', ']')[0]
    
    def current_track(self):
        """Returns the current playing artist"""
        return "%s - %s" % (self.artist, self.title)

Parser = JumpParser

if __name__ == '__main__':
    base.test_parser(Parser, 'jump.xml')
