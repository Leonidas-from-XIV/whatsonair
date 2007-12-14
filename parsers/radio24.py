#!/usr/bin/env python
# -*- encoding: UTF-8 -*-

import base, urllib

class Radio24Parser(base.StationBase):
    """Parser for Radio24"""
    
    __station__ = 'Radio24'
    __version__ = '0.2.0'
    
    def __init__(self, url='http://www.radio24.ch/ext/webradio/onair_small.php',
        stream='http://dms-cl-011.skypro-media.net/radio24-hi'):
        base.StationBase.__init__(self, url)
    
    def parse(self):
        """Cuts the content and extracts informations"""
        # get the soup
        soup = base.Soup(self.pagecontent)
        # now the hacking begins (some trouble with BeautifulSoup)
        # select an element
        point = base.select(soup, 'tr td i')[0]
        # get its parent
        parent = point.parent
        # get all texts
        texts = parent.findAll(text=True)
        # convert and save these
        artist = texts[1].strip()
        title = texts[-1].strip()
        self.artist = self.capstext(artist)
        self.title = self.capstext(title)
    
    def current_track(self):
        """Returns the current playing artist"""
        return "%s - %s" % (self.artist, self.title)

Parser = Radio24Parser

if __name__ == '__main__':
    base.test_parser(Parser, 'radio24.html')
