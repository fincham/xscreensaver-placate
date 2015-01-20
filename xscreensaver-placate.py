# xscreensaver-placate.py by Michael Fincham <michael@finch.am> 2011-05-05
# released in to the public domain

import totem, time, threading, os

class XscreensaverPlacateTimer(threading.Thread):

  is_done = False
  should_blank = True

  def run(self):
    loops = 0 
    while self.is_done == False:
      time.sleep(0.5)
      loops = loops + 1
      if loops > 60:
        loops = 0
        if self.should_blank == False:
          os.system('xscreensaver-command -deactivate >&- 2>&- &')
          
class XscreensaverPlacatePlugin(totem.Plugin):

  def __init__(self):
    totem.Plugin.__init__(self)

  def on_notify(self, totem, spec):
    if totem.is_playing() and totem.is_fullscreen():
      self.timer_thread.should_blank = False
    else:
      self.timer_thread.should_blank = True

  def activate(self, totem):
    totem.connect('notify', self.on_notify)
    self.timer_thread = XscreensaverPlacateTimer()
    self.timer_thread.start()
    self.on_notify(totem, None)

  def deactivate(self, totem):
    self.timer_thread.is_done = True
