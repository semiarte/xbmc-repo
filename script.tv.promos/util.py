import xbmc, xbmcgui, xbmcaddon, os, sys

__addon__       = xbmcaddon.Addon('script.tv.promos')
__cwd__ = xbmc.translatePath(__addon__.getAddonInfo('path')).decode("utf-8")
BASE_RESOURCE_PATH = os.path.join(__cwd__, 'resources', 'lib')
sys.path.append(BASE_RESOURCE_PATH)

import requests

def grabvideo(url, name, location):
    r = requests.get(url)
    with open(location + name + ".flv", "wb") as code:
        code.write(r.content)

def notify(message):
    __addonname__   = __addon__.getAddonInfo('name')
    __icon__        = __addon__.getAddonInfo('icon')

    timeShown = 5000  #in miliseconds
 
    xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(__addonname__,message, timeShown, __icon__))

def extract(text, startText, endText):
    start = text.find(startText, 0)
    if start != -1:
        start = start + startText.__len__()
        end = text.find(endText, start + 1)
        if end != -1:
            return text[start:end]
    return None

def PlayThis(videolink):
    playlist = xbmc.PlayList( xbmc.PLAYLIST_VIDEO )
    playlist.clear()
    playlist.add(videolink)
    xbmc.Player().play( playlist)
