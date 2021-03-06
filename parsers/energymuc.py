#!/usr/bin/env python
# -*- encoding: UTF-8 -*-

import base

class EnergyMucParser(base.StationBase):
    """Energy in Munich
    listen to it on 93.3 MHz"""
    
    __station__ = 'EnergyMunich'

    def __init__(self, url='http://www.energy.de/static/ticker/ticker.php?sender=muenchen'):    
        base.StationBase.__init__(self, url)
    
    def parse(self):
        """Call feed first"""
        self.title = self.cut_content('&song_mue=', '&&artist_mue=')[0]
        
        self.artist = self.capstext(self.cut_content('&&artist_mue=', '&')[0])

    def current_track(self):
        return u"%s - %s" % (self.artist, self.title)

Parser = EnergyMucParser

if __name__ == '__main__':
    base.test_parser(Parser, 'energy_mue.html')
    
