#!/usr/bin/env python
# -*- encoding: latin-1 -*-

import base

class Antenne1Parser(base.StationBase):
    """Parser for Antenne 1"""
    
    __station__ = 'Antenne1'
    __version__ = '0.1.0'
    
    def __init__(self, url='http://antenne1.de/index_start.php'):
        base.StationBase.__init__(self, url)
    
    def parse(self):
        """Call feed first"""
        track = self.cut_content_simple('height="5"><br>', '</td>')
        self.artist, self.title = [part.strip() for part in track[0].split('-')]
        
    def current_track(self):
        if self.title != '':
            return "%s - %s" % (self.capstext(self.artist), self.capstext(self.title))
        else:
            # no title - means "News" or things like this
            return self.artist

Parser = Antenne1Parser

if __name__ == '__main__':
    base.test_parser(Parser, 'antenne1.html')
