from PyQt5.QtWidgets import *
from lab9g import *

class Television(QMainWindow, Ui_Remote):
    '''
    Creates a 'Television'/'Remote' GUI that functions as a television. With channel/volume
    buttons a power button mute button and some imagery and volume meter for functionality.
    '''


    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    status = False
    muted = False
    volume = 0
    channel = 0

    def __init__(self, *args, **kwargs) -> None:
        '''
        This function initializes television class and creates GUI from lab9g.py
        :param args:
        :param kwargs:
        '''
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        #button clicks
        self.volumeUpButton.clicked.connect(lambda: self.volume_up())
        self.volumeDownButton.clicked.connect(lambda: self.volume_down())
        self.channelUpButton.clicked.connect(lambda: self.channel_up())
        self.channelDownButton.clicked.connect(lambda: self.channel_down())
        self.muteButton.clicked.connect(lambda: self.mute())
        self.powerButton.clicked.connect(lambda: self.power())



    def channel_up(self) -> None:
        '''
        This is used to increase the tv channel value when the tv is on.
        If the tv is on the maximum channel and this method is called, it will set
        the tv channel to the minimum channel
        :return:  -> None
        '''
        if self.status == True:
            match self.channel:
                case self.MAX_CHANNEL:
                    self.channel = self.MIN_CHANNEL
                    self.photo.setPixmap(QtGui.QPixmap("ap.png"))
                case x:
                    self.channel = x + 1
                    if self.channel == 0:
                        self.photo.setPixmap(QtGui.QPixmap("ap.png"))
                    elif self.channel == 1:
                        self.photo.setPixmap(QtGui.QPixmap("natgeo.jpg"))
                    elif self.channel == 2:
                        self.photo.setPixmap(QtGui.QPixmap("discovery.png"))
                    elif self.channel == 3:
                        self.photo.setPixmap(QtGui.QPixmap("history.png"))

    def channel_down(self) -> None:
        '''
        This is used to decrease the tv channel value when the tv is on.
        If the tv is on the minimum channel and this method is called, it sets
        the tv channel to the maximum channel.
        :return:  -> None
        '''
        if self.status == True:
            match self.channel:
                case self.MIN_CHANNEL:
                    self.channel = self.MAX_CHANNEL
                    self.photo.setPixmap(QtGui.QPixmap("history.png"))
                case x:
                    self.channel = x - 1
                    if self.channel == 0:
                        self.photo.setPixmap(QtGui.QPixmap("ap.png"))
                    elif self.channel == 1:
                        self.photo.setPixmap(QtGui.QPixmap("natgeo.jpg"))
                    elif self.channel == 2:
                        self.photo.setPixmap(QtGui.QPixmap("discovery.png"))
                    elif self.channel == 3:
                        self.photo.setPixmap(QtGui.QPixmap("history.png"))

    def volume_up(self) -> None:
        '''
        This is used to increase the tv volume when the tv is on.
        When the tv is on the maximum volume and this method is called, the volume will
        just remain at the maximum.
        If any of the volume methods were called when the tv was muted,
        it automatically unmutes the tv and adjust the tv volume accordingly.
        :return: -> None
        '''
        if self.muted == True:
            self.muted = False
            self.horizontalSlider.setSliderPosition(self.volume)
        if self.status == True:
            if self.volume < self.MAX_VOLUME:
                self.volume += 1
                self.horizontalSlider.setSliderPosition(self.volume)


    def volume_down(self) -> None:
        '''
        This is used to decrease the tv volume when the tv is on.
        If the tv is on the mimmum volume and this method is called,
        the volume will just remain at the minimum.
        If any of the volume methods were called when the tv was muted,
        it automatically unmutes the tv and adjust the tv volume accordingly.

        :return: -> None
        '''
        if self.muted == True:
            self.muted = False
            self.horizontalSlider.setSliderPosition(self.volume)
        if self.status == True:
            if self.volume > self.MIN_VOLUME:
                self.volume -= 1
                self.horizontalSlider.setSliderPosition(self.volume)

    def mute(self) -> None:
        '''
        This is used to
        mute and unmute the tv when it's on by changing the value of the muted variable.
        :return: -> None
        '''
        if self.status == True:
            if self.muted == True:
                self.muted = False
            elif self.muted == False:
                self.muted = True
                self.horizontalSlider.setSliderPosition(0)

    def power(self) -> None:
        '''
        This is used to turn the tv on and off by changing the
        value of the status variable.
        :return:
        '''
        if self.status == False:
            self.status = True
            if self.channel == 0:
                self.photo.setPixmap(QtGui.QPixmap("ap.png"))
            elif self.channel == 1:
                self.photo.setPixmap(QtGui.QPixmap("natgeo.jpg"))
            elif self.channel == 2:
                self.photo.setPixmap(QtGui.QPixmap("discovery.png"))
            elif self.channel == 3:
                self.photo.setPixmap(QtGui.QPixmap("history.png"))
        elif self.status == True:
            self.status = False
            self.photo.setPixmap(QtGui.QPixmap("black.jpg"))

    def __str__(self) -> None:
        '''
        Old function for basic print functionality instead of using GUI.
        Prints Power status, Channel number, Volume number.
        :return: -> None
        '''
        if self.muted == True:
            return f'TV status: Power = {self.status}, Channel = {self.channel}, Volume = 0'
        else:
            return f'TV status: Power = {self.status}, Channel = {self.channel}, Volume = {self.volume}'