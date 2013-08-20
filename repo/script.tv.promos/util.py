import xbmc, xbmcaddon

def notify(message):
    __addon__       = xbmcaddon.Addon('script.tv.promos')
    __addonname__   = __addon__.getAddonInfo('name')
    __icon__        = __addon__.getAddonInfo('icon')

    timeShown = 5000  #in miliseconds
 
    xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(__addonname__,message, timeShown, __icon__))
