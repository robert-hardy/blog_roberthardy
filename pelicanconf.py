#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Robert Hardy'
SITENAME = 'roberthardy.io'
SITEURL = ''
BIO = u"I am a quant at MAN. I use computers and maths every day."

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (
    ('LinkedIn', 'https://uk.linkedin.com/in/roberthardyuk'),
    ('Github', 'https://github.com/robert-hardy'),
    ('Stack Overflow', 'http://stackoverflow.com/users/1243435/robert'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Bring reports into output but do not process them.
STATIC_PATHS=['images', 'reports', 'CNAME', 'apps']
ARTICLE_EXCLUDES=['reports', 'apps']

# Fix navbar order by taking full control
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

MENUITEMS = (
    ('Home', '/'),
    ('About', 'pages/about.html'),
    ('Blog', '/index_blog.html'),
    ('Data', '/pages/data-sources.html')
    )


# Home page for the blog articles.
INDEX_SAVE_AS='index_blog.html'
