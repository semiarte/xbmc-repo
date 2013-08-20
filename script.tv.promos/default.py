# Import the modules
import urllib,urllib2,re
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
import sys, util
import json
import requests

__addon__       = xbmcaddon.Addon()
__addonname__   = __addon__.getAddonInfo('name')
__icon__        = __addon__.getAddonInfo('icon')

time = 5000  #in miliseconds

class MyPlayer(xbmc.Player):
    def __init__(self, *args):
        xbmc.Player.__init__(self)

    def onPlayBackStarted(self):
        __setting__   = xbmcaddon.Addon('script.tv.promos').getSetting("StreamUrl")
        varYoutubeSI = xbmcaddon.Addon('script.tv.promos').getSetting("StreamUrl")
        
        if __setting__ == 'Youtube':
        #START YOUTUBE CODE
            if xbmc.getInfoLabel("VideoPlayer.TVShowTitle") == '':
                self.varHasPlayed = "Yes"
            else:
                self.varHasPlayed = "No"
                EpisodeTmp = xbmc.getInfoLabel("VideoPlayer.Episode")
                EpisodeNumber = int(EpisodeTmp) + int(1)
                varSearchString = xbmc.getInfoLabel("VideoPlayer.TVShowTitle") + " " + xbmc.getInfoLabel("VideoPlayer.Season") + "x" + str(EpisodeNumber) + " promo"

                # Set Headers
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3',
                }

                # Get the feed
                r = requests.get("http://gdata.youtube.com/feeds/api/videos?q=" + varSearchString + "&start-index=" + varYoutubeSI + "&max-results=1&v=2&alt=jsonc", headers=headers)
                r.text
 
                # Convert it to a Python dictionary
                data = json.loads(r.text)
 
                # Loop through the result. 
                for item in data['data']['items']:
 
                    self.varVideoID = item['id']

                xbmc.sleep(1000)
        #END YOUTUBE CODE
        if __setting__ == 'Tv Rage':
            util.notify("Under Construction")

    def onPlayBackEnded(self):
        if self.varHasPlayed == "Yes":
            pass
        else:
            __setting1__ = xbmcaddon.Addon('script.tv.promos').getSetting("StreamUrl")

            if __setting1__ == 'Youtube':
                xbmc.executebuiltin("XBMC.PlayMedia(plugin://plugin.video.youtube/?action=play_video&videoid=" + self.varVideoID + ")")

            if __setting1__ == 'Tv Rage':
                util.notify=("Under Construction")

    def onPlaybackStopped(self):
        pass

xbmc.log("script.tv.promos: Started Running")

player = MyPlayer()
        
while(not xbmc.abortRequested):
    xbmc.sleep(100)

xbmc.log("script.tv.promos: Finished Running")
