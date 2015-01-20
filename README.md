# xscreensaver-placate

This function was [added to Totem in 2003-ish](http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=208175) but subsequently removed at some point owing to a percieved "lack of maintenance" of [XScreenSaver](http://www.jwz.org/xscreensaver/).

See below a simple plugin which will call `xscreensaver-command -deactivate >&- 2>&- &` once per minute while Totem is both playing and fullscreened. This effectively prevents XScreenSaver from blanking while a video is playing in fullscreen.

The code is very simple and could be easily adapted as a generic "watchdog" plugin for Totem to run an arbitrary command at arbitrary intervals under configurable conditions. I have tested it a bit but not a lot. Bug reports are welcomed.

To install, either drop the two files below in to `~/.local/share/totem/plugins/` to install the plugin for the current user, or in to `/usr/lib/totem/plugins/` to install the plugin systemwide. 
