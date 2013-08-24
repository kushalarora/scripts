import urllib2
import shutil
from BeautifulSoup import BeautifulSoup
import re

DIR_PATH = "/extra/Fall2013/MIS/"
URL_PATH = "http://ia700306.us.archive.org/22/items/MIT18.06S05_MP4/"
EXT = "mp4"

pattern = re.compile("/?([^\.]+)." + EXT)
for link in BeautifulSoup(urllib2.urlopen(URL_PATH).read()).findAll("a"):
    match = pattern.search(link["href"])
    if match:
        response = urllib2.urlopen(URL_PATH + link["href"])
        out_file = open(DIR_PATH + match.group(1) + "." + EXT, 'wb')
        shutil.copyfileobj(response, out_file)

