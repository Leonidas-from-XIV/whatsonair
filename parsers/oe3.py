#!/usr/bin/env python
# -*- encoding: UTF-8 -*-

import base, fm4

class OE3Parser(fm4.FM4Parser):
    """�3 parser
    http://oe3.orf.at"""
    
    __station__ = 'OE3'
    
    def __init__(self, url='http://hop.orf.at/img-trackservice/oe3.html'):
        base.StationBase.__init__(self, url)

Parser = OE3Parser

if __name__ == '__main__':
    base.test_parser(Parser, 'oe3.html')
