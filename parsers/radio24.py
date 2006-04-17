#!/usr/bin/env python
# -*- encoding: latin-1 -*-

import base, urllib

class Radio24Parser(base.StationBase):
    """Parser for Radio24"""
    
    __station__ = 'Radio24'
    __version__ = '0.1.1'
    
    def __init__(self, url='http://www.radio24.ch/php/now_playing.php',
        stream='http://dms-cl-011.skypro-media.net/radio24-hi'):
        base.StationBase.__init__(self, url)
    
    def parse(self):
        """Cuts the content and extracts informations"""
        
        # split on the &
        infos = self.pagecontent.split('&')
        
        # feed the variables artist and title with the values
        for info in infos:
            if info.startswith('interpret='):
                artist = info.replace('interpret=', '')
            elif info.startswith('song='):
                title = info.replace('song=', '')
        
        # replace the + by a space
        self.artist = artist.replace('+', ' ')
        # as previous, but additionally unquote the HTTP-styled quotes
        self.title = urllib.unquote(title.replace('+', ' '))
    
    def current_track(self):
        """Returns the current playing artist"""
        return "%s - %s" % (self.capstext(self.artist), self.capstext(self.title))

Parser = Radio24Parser

if __name__ == '__main__':
    base.test_parser(Parser, 'radio24.html')
