import itunes as it


# Launch iTune
def launch():
    it.activate()


# play iTune
def play():
    it.play()


# play next song
def next():
    it.next()


# play previous song
def previous():
    it.prev()


# stop the music
def stop():
    it.stop()


# get state of iTune
def state():
    return it.state()


# pause the music
def pause():
    it.pause()


# mute iTune
def mute():
    it.mute()


# un mute iTune
def un_mute():
    it.unmute()
