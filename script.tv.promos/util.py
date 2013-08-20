import xbmc, xbmcgui, xbmcaddon

def notify(message):
    __addon__       = xbmcaddon.Addon('script.tv.promos')
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

def playMedia(title, thumbnail, link, mediaType='Video') :
    li = xbmcgui.ListItem(label=title, iconImage=thumbnail, thumbnailImage=thumbnail, path=link)
    li.setInfo(type=mediaType, infoLabels={ "Title": title })
    xbmc.Player().play(item=link, listitem=li)

def PlayThis(videolink):
    playlist = xbmc.PlayList( xbmc.PLAYLIST_VIDEO )
    playlist.clear()
    playlist.add(videolink)
    xbmc.Player().play( playlist)
    xbmc.sleep(1000)
    xbmc.Player().pause()
