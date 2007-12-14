#!/usr/bin/env python
# -*- encoding: UTF-8 -*-

import base

class LandesWelleParser(base.StationBase):
    """Parser for LandesWelle"""
    
    __station__ = 'Landeswelle'
    
    def __init__(self, url='http://www.landeswelle.de/lwt/components/flash/index_lwt.php'):
        base.StationBase.__init__(self, url)
    
    def parse(self):
        """Call feed first"""
        divided = self.pagecontent.split('#')
        self.title = self.capstext(divided[1].split('=')[1])
        self.artist = self.capstext(divided[2].split('=')[1])
    
    def current_track(self):
        return u"%s - %s" % (self.artist, self.title)

Parser = LandesWelleParser

if __name__ == '__main__':
    base.test_parser(Parser, 'lwt.html')

