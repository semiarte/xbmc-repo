import xbmc, xbmcaddon, xbmcgui
import os

__addon__       = xbmcaddon.Addon('script.tv.promos')

class TextBox:
    # constants
    WINDOW = 10147
    CONTROL_LABEL = 1
    CONTROL_TEXTBOX = 5

    def __init__(self, *args, **kwargs):
        # activate the text viewer window
        xbmc.executebuiltin("ActivateWindow(%d)" % ( self.WINDOW, ))
        # get window
        self.win = xbmcgui.Window(self.WINDOW)
        # give window time to initialize
        xbmc.sleep(1000)
        self.setControls()

    def setControls(self):
        # set heading
        heading = "TV Promos Version - %s" % (__addon__.getAddonInfo('version'))
        self.win.getControl(self.CONTROL_LABEL).setLabel(heading)
        # set text
        root = __addon__.getAddonInfo('path')
        changelog_path = os.path.join(root, 'changelog.info')
        f = open(changelog_path)
        text = f.read()
        self.win.getControl(self.CONTROL_TEXTBOX).setText(text)
