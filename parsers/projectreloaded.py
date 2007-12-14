#!/usr/bin/env python
# -*- encoding: UTF-8 -*-

import base, urllib2, time, re

class ProjectReloadedParser(base.StationBase):
    """Parser for Project-Reloaded
    Homepage: http://www.project-reloaded.com/
    Stream  : http://62.26.4.172:8010/;stream.nsv
              rtsp://62.26.161.89/projectreloaded$livestream.wma"""
    __station__ = 'Project Reloaded'
    __version__ = '0.0.1'

    def __init__(self, url=None):
        if url is None:
            url = time.strftime('http://schueler.homeip.net/project-reloaded/search.php?day=%d&month=%m&hour=%H&minute=%M')
        # call the parent
        base.StationBase.__init__(self, url)

    def parse(self):
        try:
            self.artist = re.findall('<td class="artist" .*?>(.*?)</td>', self.pagecontent)[-1]
            self.title  = re.findall('<td class="title" .*?>(.*?)</td>', self.pagecontent)[-1]
        except IndexError:
            self.artist, self.title = (None,) * 2

    def current_track(self):
        if self.artist is not None and self.title is not None:
            return "%s - %s" % (self.artist, self.title)
        else:
            # TODO: let this raise a proper exception (or parse)
            return 'No song playing at the moment'

Parser = ProjectReloadedParser

if __name__ == '__main__':
    base.test_parser(Parser, 'projectreloaded.html')
