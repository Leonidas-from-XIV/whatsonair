#!/usr/bin/env python
# -*- encoding: UTF-8 -*-

import base

class FM4Parser(base.StationBase):
    """The Parser for the austrian sidestream radio station
    FM4, which is part of ORF.
    Look at it's homepage http://fm4.orf.at
    
    Maybe besser use this songlist?
    http://fm4.orf.at/trackservicepopup/main
    But then we loose the ability to parse OE3 as well"""
    
    __station__ = 'FM4'
    
    def __init__(self, url='http://hop.orf.at/img-trackservice/fm4.html',
        stream='mms://stream1.orf.at/fm4_live'):
        base.StationBase.__init__(self, url)
    
    def parse(self):
        """Call feed first"""
        # get the titles and the artists
        soup = base.Soup(self.pagecontent)
        titles = [node.string for node in
                base.select(soup, 'span.tracktitle')]
        artists = [node.string for node in
                base.select(soup, 'span.artist')]

        # combine these
        combined = zip(artists, titles)
        # get the last artist and title
        self.artist, self.title = combined[-1]
    
    def current_track(self):
        return u"%s - %s" % (self.artist, self.title)

Parser = FM4Parser

if __name__ == '__main__':
    base.test_parser(Parser, 'fm4.html')
    
