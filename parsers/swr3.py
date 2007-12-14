#!/usr/bin/env python
# -*- encoding: latin-1 -*-

import base, re

class SWR3Parser(base.StationBase):
    """Parser for SWR 3"""
    
    __station__ = 'SWR3'
    __version__ = '0.2.0'
    
    def __init__(self, url='http://www.swr3.de/musik/musikrecherche/-/id=47424/nid=47424/did=202234/1213ds4/index.html',
        stream='rtsp://195.52.221.172/farm/*/encoder/swr3/livestream.rm'):
        base.StationBase.__init__(self, url)
    
    def parse(self):
        """Call feed first"""
        soup = base.Soup(self.pagecontent)
        elements = [element.string for element in
                base.select(soup, 'table tr a')]
        artists = elements[0::2]
        titles = elements[1::2]
        combined = zip(artists, titles)

        artist, self.title = combined[0]
        self.artist = self.uncommafy(artist)
    
    def current_track(self):
        return u"%s - %s" % (self.artist, self.title)

Parser = SWR3Parser

if __name__ == '__main__':
    base.test_parser(Parser, 'last13html.html')
