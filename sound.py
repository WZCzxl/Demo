from pygame import mixer

class Sound(object):

    def __init__(self):
        self.ships_move_sound = 9
        self.switch = {1: "musics/expl3.wav", 2: "musics/expl6.wav", 3: "musics/getready.ogg",
                       4: "musics/menu.ogg", 5: "musics/pew.wav", 6: "musics/rocket.ogg",
                       7: "musics/rumble1.ogg", 8: "musics/tgfcoder-FrozenJam-SeamlessLoop.ogg"}
        try:
            self.sound = mixer.Sound(self.switch[self.ships_move_sound])
        except KeyError:
            self.sound = mixer.Sound(self.switch[1])

    def sound_play(self):
        self.sound.play(loops=-1)

    def sound_stop(self):
        self.sound.stop()