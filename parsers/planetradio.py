#!/usr/bin/env python
# -*- encoding: UTF-8 -*-

import base, re

timestamp = re.compile(r'\d\d\.\d\d \d\d:\d\d')

class PlanetRadioParser(base.StationBase):
    """Parser for PlanetRadio"""
    
    __station__ = 'PlanetRadio'
    
    def __init__(self, url='http://www.planetradio.de/p_mt.php'):
        base.StationBase.__init__(self, url)
    
    def parse(self):
        """Call feed first"""
        soup = base.Soup(self.pagecontent)

        heading_last = base.select(soup, 'h2')[-1]
        track_table = heading_last.findNextSibling()
        tds = track_table.findAll('td')
        useful = list()
        for td in tds:
            if not td.findAll('a'):
                # filter out non breaking spaces
                if td.string == '&nbsp;':
                    continue
                # filter out dates
                if timestamp.match(td.string):
                    continue
                useful.append(td)

        # group them into (title, artist)
        tracks = [(useful[a], useful[a+1]) for a in range(0, len(useful), 2)]

        self.title = self.capstext(tracks[0][0].string)
        self.artist = self.capstext(tracks[0][1].string)
    
    def current_track(self):
        return u"%s - %s" % (self.artist, self.title)

Parser = PlanetRadioParser

if __name__ == '__main__':
    base.test_parser(Parser, 'planetradio.html')
