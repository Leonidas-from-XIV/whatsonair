#!/usr/bin/env python
# -*- encoding: UTF-8 -*-

import base

class NJoyParser(base.StationBase):
    """NJoy"""
    
    __station__ = 'NJoy'
    
    def __init__(self, url='http://www1.n-joy.de/pages_special/0,,SPM2156,00.html'):
        base.StationBase.__init__(self, url)
    
    def parse(self):
        """Call feed first"""
        # get rid of annoying linebreaks
        self.pagecontent = self.pagecontent.replace('\n', '')
        
        artists = self.cut_content('<td headers="headerB">', '</td>')
        titles = self.cut_content('<td headers="headerC">', '</td>')
        both = zip(artists, titles)

        try:
            self.artist, self.title = both[-1]
            self.artist = self.capstext(self.artist)
        except IndexError:
            raise ValueError('There is currently no song')
    
    def current_track(self):
        return u"%s - %s" % (self.artist, self.title)

Parser = NJoyParser

if __name__ == '__main__':
    base.test_parser(Parser, 'njoy.html')
    
