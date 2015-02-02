import os, re, time
import threading
import urllib, urllib2, HTMLParser
import datetime
import simplejson
from BeautifulSoup import BeautifulSoup

SF_ROOT     = 'http://www.srf.ch'
SENDUNG     = SF_ROOT + '/play/tv/episodesfromshow'
PAGENR      = '1'
# SENDUNG     = SF_ROOT + '/play/tv/sendung/aeschbacher'
ID          = '0a7932df-dea7-4d8a-bd35-bba2fe2798b5'

def getIdFromUrl(url):
    return re.compile( '[\?|\&]id=([0-9a-z\-]+)').findall( url)[0]

# Get JSON for the Playlist items
def fetchHttp( url, args={}, hdrs={}, post=False):
    print url
    hdrs["User-Agent"] = "Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0"
    if post:
        req = urllib2.Request( url, urllib.urlencode( args), hdrs)
    else:
        url = url + "?" + urllib.urlencode( args)
        req = urllib2.Request( url, None, hdrs)
    response = urllib2.urlopen( req)
    encoding = re.findall("charset=([a-zA-Z0-9\-]+)", response.headers['content-type'])
    text = response.read()
    if len(encoding):
        responsetext = unicode( text, encoding[0] );
    else:
        responsetext = text
    response.close()

    return responsetext


def fetchHttp( url, args={}, hdrs={}, post=False):
    hdrs["User-Agent"] = "Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0"
    if post:
        req = urllib2.Request( url, urllib.urlencode( args), hdrs)
    else:
        url = url + "?" + urllib.urlencode( args)
        req = urllib2.Request( url, None, hdrs)
    response = urllib2.urlopen( req)
    encoding = re.findall("charset=([a-zA-Z0-9\-]+)", response.headers['content-type'])
    text = response.read()
    if len(encoding):
        responsetext = unicode( text, encoding[0] );
    else:
        responsetext = text
    response.close()

    return responsetext
 
def getUrlWithoutParams( url):
    return url.split('?')[0]
  
# Loop through Episodes
soup = BeautifulSoup(fetchHttp(SENDUNG,{"id": ID, "pageNumber": PAGENR}))
for show in soup.findAll( "li", "sendung_item"):
    title = show.find( "h3", "title").text
    titleDate = show.find( "div", "title_date").text
#     image = getUrlWithoutParams(show.find( "img")['src'])
    a = show.find("a").findNext("a")
    sendid = getIdFromUrl(a['href'])
    episodeurl = SF_ROOT + getUrlWithoutParams(a['href'])
    print episodeurl
    try:
        sendsoup = BeautifulSoup(fetchHttp(episodeurl,{"id": sendid}))
    except:
            pass
    print sendsoup.findAll("meta",{"property":"og:video"})
    b = str(sendsoup.findAll("meta",{"property":"og:video"}))
    print b[35:-5]
    






    
