#!/usr/bin/env python
# -*- encoding: UTF-8 -*-

import base, hr3

class HR4Parser(hr3.HR3Parser):
    """HR4"""
    
    __station__ = 'HR4'
    
    def __init__(self, url='http://www3.admin.hr-online.de/playlist/playlist.php?tpl=hr4'):
        base.StationBase.__init__(self, url)

Parser = HR4Parser

if __name__ == '__main__':
    base.test_parser(Parser, 'hr4.html')
    
