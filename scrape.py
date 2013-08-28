from urllib2 import urlopen
from urllib import unquote_plus
import shutil
from BeautifulSoup import BeautifulSoup
import re

DIR_PATH = "/extra/Fall2013/ADS/PPT/"
URL_PATH="http://www.cise.ufl.edu/~sahni/cop5536/powerpoint/"
#URL_PATH = "http://ia700306.us.archive.org/22/items/MIT18.06S05_MP4/"
EXT = "ppt"

pattern = re.compile("/?([^\.]+)." + EXT)
for link in BeautifulSoup(urlopen(URL_PATH).read()).findAll("a"):
    match = pattern.search(link["href"])
    if match:
        response = urlopen(URL_PATH + link["href"])
        out_file = open(DIR_PATH + unquote_plus(match.group(1)) + "." + EXT, 'wb')
        shutil.copyfileobj(response, out_file)

