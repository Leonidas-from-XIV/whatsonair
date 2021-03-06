#!/usr/bin/env python
# -*- encoding: UTF-8 -*-

import base

class EnergySaxParser(base.StationBase):
    """Energy in Saxonia"""
    
    __station__ = 'EnergySaxonia'
    
    def __init__(self, url='http://www.energy.de/static/ticker/ticker.php?sender=sachsen'):
        base.StationBase.__init__(self, url)
    
    def parse(self):
        """Call feed first"""
        track = self.cut_content_simple('&song_sac=JETZT: ', '&&artist_sac=')[0]
        artist, title = track.split(' - ', 1)
        self.artist = self.capstext(artist)
        self.title = self.capstext(title)
    
    def current_track(self):
        return u"%s - %s" % (self.artist, self.title)

Parser = EnergySaxParser

if __name__ == '__main__':
    base.test_parser(Parser, 'sach.html')
    
