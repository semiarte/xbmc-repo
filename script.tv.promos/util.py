import xbmc, xbmcgui, xbmcaddon
from classfile import *

__addon__       = xbmcaddon.Addon('script.tv.promos')
__addonname__   = __addon__.getAddonInfo('name')
__icon__        = __addon__.getAddonInfo('icon')

def notify(message):
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

def CheckforUpdate():
    old_version = __addon__.getSetting('VersionNumber').replace(".", "")
    new_version = __addon__.getAddonInfo('version').replace(".", "")
    varShowChanges = __addon__.getSetting('ShowChanges')
    if int(old_version) < int(new_version):
        if varShowChanges == 'Yes':
            dialog = xbmcgui.Dialog()
            i = dialog.yesno(__addonname__, "Would you like to display the changelog?")

            if i == 0:
                pass
            else:
                TextBox()
        else:
            pass

        __addon__.setSetting('VersionNumber', __addon__.getAddonInfo('version'))
    else:
        pass
    
