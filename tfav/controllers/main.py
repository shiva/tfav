import logging
import feedparser
import operator
import time
import re

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from tfav.lib.base import BaseController, render

#List of uples (label, property-tag, truncation)
COMMON_CHANNEL_PROPERTIES = [
    ('Channel title:', 'title', None),
    ('Channel description:', 'description', 100),
    ('Channel URL:', 'link', None),
]

COMMON_ITEM_PROPERTIES = [
    ('Item title:', 'title', None),
    ('Item description:', 'description', 100),
    ('Item URL:', 'link', None),
]

INDENT = u' '*4

log = logging.getLogger(__name__)

class Tweet:
	def __init__(self):
		self.data = []
		
class MainController(BaseController):

	def convertToHtmlLink(self, match):
		"Return html version of link"
		return '<a href="' + match.group(0) + '">' + match.group(0) + '</a>'
		
	def index(self):
		try :
			c.user = request.params['uname']
		except KeyError :
			c.user = 'shiva'
		
		if len(c.user) < 1:
			c.user = 'shiva'
		
		feeds = ('http://twitter.com/favorites/'+c.user +'.rss?page=1',)
        
		feeds = map(lambda x : feedparser.parse(x).entries, feeds)
		feeds = reduce(operator.concat, feeds)
		feeds = sorted(feeds, lambda x,y : cmp(y.date_parsed, x.date_parsed))
		
		regex = re.compile(r'\b((https?|ftp|file)://[-A-Z0-9+&@#/%?=~_|!:,.;]*[-A-Z0-9+&@#/%=~_|])', re.DOTALL|re.IGNORECASE)
		c.favs = list()
		sep = ':'
		for entry in feeds:
			fav = Tweet()
			fav.desc = entry.title
			(fav.author, sep, tweet) = fav.desc.partition(sep)
			fav.tweet = regex.sub(self.convertToHtmlLink, tweet)
			fav.time = entry.date_parsed
			fav.link = entry.link
			c.favs.append(fav)
			
		return render('/main.mako')
