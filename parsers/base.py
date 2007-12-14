#!/usr/bin/env python
# -*- encoding: UTF-8 -*-

# stdlib imports
import urllib, re
# beautiful soup (or some module with a BS interface)
from BeautifulSoup import BeautifulSoup as Soup
# soup select for CSS selectors
from soupselect import select

class StationBase(object):
    """The base class for each radio station parser
    provides already some rough tools like the HTMLParser.
    The defined methods should be overloaded to provide a
    consistent interface for all derived station parsers
    
    The constructor loads the page content into self.pagecontent,
    and also cares about timeout handling. So in child classes
    you need to call StationBase.__init__ for doing the most work.
    
    All child classes also have a feed() method, where the page content
    is parsed and all values initialized. After that, curent_track() can
    be called to get the currently playing track."""
    __station__ = 'StationBase'
    __version__ = '1.1.0'
    
    def __init__(self, url, stream=None):
        """Initialize some values."""
        self.crawler_url = url
        self.stream_url = stream
        self.pagecontent = None
    
    def feed(self):
        """Loads the page content from the internet"""
        # get the default timeout
        timeout = urllib.socket.getdefaulttimeout()
        # set the new timeout to ten seconds
        urllib.socket.setdefaulttimeout(10.0)
        
        # open the page to read and get the content
        parsepage = urllib.urlopen(self.crawler_url)
        self.pagecontent = parsepage.read()
        #self.soup = Soup(self.pagecontent)

        # close the page and re-set the timeout
        parsepage.close()
        urllib.socket.setdefaulttimeout(timeout)
    
    def current_track(self):
        """Return the current track in the format
        ARTIST - TITLE as unicode object"""
        raise NotImplementedError("Abstract class")
    
    def capstext(self, text):
        """A helper method to make the texts look consistent
        [...]"""
        chunks = text.split()
        
        if len(chunks) > 1:
            return reduce(lambda x, y: x.capitalize() + ' ' + y.capitalize(), chunks)
        else:
            return text.capitalize()
    
    def create_regexp(self, start, stop):
        """Creates regular expressions"""
        # this expression is non-greedy: it uses .*? instead of .*
        reg_exp_code = r'(?<=%s).*?(?=%s)' % (start, stop)
        compiled = re.compile(reg_exp_code)
        return compiled
    
    def cut_content(self, start, stop, content=True):
        """This is to be called by the plugins
        Content is the content to be searched."""
        start = self.escape_specialchars(start)
        stop = self.escape_specialchars(stop)
        
        rex = self.create_regexp(start, stop)
        if content == True:
            return rex.findall(self.pagecontent)
        else:
            # else match the provided content
            return rex.findall(content)

    def cut_content_simple(self, start, stop, content=True):
        content = self.pagecontent
        scanning = True
        startpoint = -1
        chunks = list()
        while scanning:
            try:
                startpoint = content.index(start, startpoint + 1)
                stoppoint = content.index(stop, startpoint + 1)
                chunkstart = startpoint + len(start)

                chunks.append(content[chunkstart:stoppoint])
            except ValueError:
                return chunks

    def escape_specialchars(self, regexp):
        """Escapes special characters in regular expressions"""
        # special characters to escape
        escapechars = ['\\', '[', ']', '(', ')']
        
        for char in escapechars:
            regexp = regexp.replace(char, '\\' + char)
        
        return regexp

Parser = None

def test_parser(parser, filename):
    """This is used to test newly written parsers.
    Import this module from a plugin using
    import base
    and then call base.test_parser(parser, filename).
    It starts the parser, sets it up and tries to get the current title.
    
    Your parsers should pass this test, means they should print the 
    correct data.
    """
    p = parser()
    f = file(filename, 'r')
    p.pagecontent = f.read()
    f.close()
    p.parse()
    print p.current_track()
