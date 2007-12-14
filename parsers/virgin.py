#!/usr/bin/env python
# -*- encoding: UTF-8 -*-

import base

class VirginParser(base.StationBase):
    """Parser for Virgin Radio: the music we all love"""
    
    __station__ = 'Virgin'
    
    def __init__(self, url='http://mangle.smgradio.com/vr.js'):
        base.StationBase.__init__(self, url)
    
    def parse(self):
        """Parses the files served by Mrs Mangle"""
        info_string = self.cut_content('var gimpdata="', '"')[0]
        informations = info_string.split('~')
        self.artist = informations[0]
        self.title = informations[2]
    
    def current_track(self):
        """Returns the current playing artist
        in the format: artist - title.
        Returns None when there is nothing interesting to display"""
        if self.title != '' or self.title != '':
            return u"%s - %s" % (self.artist, self.title)
        else:
            return None

Parser = VirginParser

if __name__ == '__main__':
    base.test_parser(Parser, 'vr.js')
