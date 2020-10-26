#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import bulrush


AUTHOR = "David O'Dwyer"
SITENAME = 'vaillant.io'
SITETITLE = 'vaillant.io'
SITEURL = ''
SITESUBTITLE = 'A sequence of writings.'
SITELOGO = SITEURL + '/images/profile.png'
# FAVICON = SITEURL + '/images/favicon.ico'

ROBOTS = 'index, follow'
CC_LICENSE = {
        'name': 'Creative Commons Attribution-ShareAlike',
        'version': '4.0',
        'slug': 'by-sa'
}

COPYRIGHT_YEAR = 2020

#SITEURL = 'D-Vaillant.github.io'  # can do redirect to vaillant.io
# SITEURL = 'vaillant.io'

PATH = 'content'

THEME = bulrush.PATH
JINJA_ENVIRONMENT = bulrush.ENVIRONMENT
JINJA_FILTERS = bulrush.FILTERS

READERS = {'html': None}

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = tuple()

# Social widget
SOCIAL = tuple()

DEFAULT_PAGINATION = 7

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['assets']

PATH_METADATA = ".*/(?P<title>.*).md"

STATIC_PATHS = ['extra']
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'custom.css'},
}
