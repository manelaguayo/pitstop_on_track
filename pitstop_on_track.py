
#PIT STOP CONFIG ON TRACK (REAL TIME) PLUGIN

import sys
import ac
import acsys

def acMain(ac_version):
    appWindow = ac.newApp("pitstop_on_track")
    ac.setSize(appWindow, 300, 300)
    return "pitstop_on_track"

ac.log("Hello, Assetto Corsa application world!")
ac.console("Hello, Assetto Corsa console!")

