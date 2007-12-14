#!/usr/bin/env python
# -*- encoding: latin-1 -*-

import base

class AntenneParser(base.StationBase):
    """Parser for Antenne Bayern"""
    
    __station__ = 'AntenneBayern'
    __version__ = '0.6.2'
    
    def __init__(self, url='http://webradio.antenne.de/antenne/webradio/new_channels/ant_infos.php',
        stream='http://webradio.antenne.de/antenne/webradio/new_channels/player_ant_mp3_url.m3u'):
        base.StationBase.__init__(self, url)
    
    def parse(self):
        """Call feed first"""
        artists = self.cut_content('<b>', '</b>')
        self.artist = artists[1]
        
        titles = self.cut_content('</b>, ', '</a>')
        self.title = titles[0]
    
    def current_track(self):
        if self.title != '':
            return "%s - %s" % (self.capstext(self.artist), self.capstext(self.title))
        else:
            # no title - means "News" or things like this
            return self.artist

Parser = AntenneParser

if __name__ == '__main__':
    base.test_parser(Parser, 'ant_infos.html')
