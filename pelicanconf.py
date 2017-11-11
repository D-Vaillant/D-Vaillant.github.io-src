#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'D. Vaillant'
SITENAME = 'vaillant.io'
SITETITLE = 'vaillant.io'
SITESUBTITLE = 'A sequence of writings by D. Vaillant.'
SITEURL = ''
SITELOGO = SITEURL + '/images/profile.png'
# FAVICON = SITEURL + '/images/favicon.ico'

ROBOTS = 'index, follow'
CC_LICENSE = {
        'name': 'Creative Commons Attribution-ShareAlike',
        'version': '4.0',
        'slug': 'by-sa'
}

COPYRIGHT_YEAR = 2017

SITEURL = 'D-Vaillant.github.io'  # can do redirect to vaillant.io

PATH = 'content'
THEME = 'Flex'

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
