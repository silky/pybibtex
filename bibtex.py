'''Utilities for formatting data to BibTeX format'''

import re

def format(data, reftype="article"):
    '''Formats a dict into a BibTeX entry'''
    entry = "@{0}{{\n".format(reftype)
    for key, val in data.iteritems():
        entry += "\t{0} = {{{1}}},\n".format(key, val)
    entry += "}}"
    return entry.encode('utf8')

def wrap(string):
    '''Wrap all capital letters in curly braces to preserve their
    capitalisation when output in LaTeX'''
    return re.sub(r'([A-Z]+)', r'{\1}', string)
