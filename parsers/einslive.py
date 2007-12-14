#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import base

class EinsLiveParser(base.StationBase):
    """Parser for EinsLive"""
    
    __station__ = 'EinsLive'
    __version__ = '0.2.0'
    
    def __init__(self, url='http://www.einslive.de/musik/playlists/'):
        base.StationBase.__init__(self, url)
    
    def parse(self):
        """Call feed first"""
        # create the soup and convert HTML entities
        soup = base.Soup(self.pagecontent, convertEntities='html')
        
        # list of artists and their tracks
        tracks = list()

        # get all elements which are td.bold (that's the artists)
        artists = base.select(soup, 'td.bold')

        for artist in artists:
            # find the next element (being hopefully the title)
            title = artist.findNextSibling()
            # append the artists name and title to the list
            tracks.append((artist.string, title.string))

        self.artist, self.title = tracks[0]
    
    def current_track(self):
        return "%s - %s" % (self.artist, self.title)

Parser = EinsLiveParser

if __name__ == '__main__':
    base.test_parser(Parser, 'einslive.html')
