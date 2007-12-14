#!/usr/bin/env python
# -*- encoding: UTF-8 -*-

import base

class AntenneThueringenParser(base.StationBase):
    """Parser for Antenne Thueringen"""
    
    __station__ = 'AntenneThueringen'
    
    def __init__(self, url='http://www.antennethueringen.de/sammler/kaufen.php'):
        base.StationBase.__init__(self, url)
    
    def parse(self):
        """Call feed first"""
        track = self.cut_content('keyword=', '" target')[0]
        self.artist, self.title = track.split(' - ')
        
    
    def current_track(self):
        return "%s - %s" % (self.artist, self.title)

Parser = AntenneThueringenParser

if __name__ == '__main__':
    base.test_parser(Parser, 'at_buy.html')

