# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lab9.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Remote(object):
    def setupUi(self, Remote) -> None:
        '''
        Created by PyQt5. Function is used to setup initial GUI for Ui_Remote class.
        :param Remote:
        :return: -> None
        '''
        Remote.setObjectName("Remote")
        Remote.resize(545, 637)
        Remote.setMinimumSize(QtCore.QSize(545, 637))
        Remote.setMaximumSize(QtCore.QSize(545, 637))
        font = QtGui.QFont()
        font.setPointSize(14)
        Remote.setFont(font)
        self.centralwidget = QtWidgets.QWidget(Remote)
        self.centralwidget.setObjectName("centralwidget")
        self.channelUpButton = QtWidgets.QPushButton(self.centralwidget)
        self.channelUpButton.setGeometry(QtCore.QRect(350, 450, 121, 31))
        self.channelUpButton.setObjectName("channelUpButton")
        self.channelDownButton = QtWidgets.QPushButton(self.centralwidget)
        self.channelDownButton.setGeometry(QtCore.QRect(350, 500, 121, 31))
        self.channelDownButton.setObjectName("channelDownButton")
        self.volumeUpButton = QtWidgets.QPushButton(self.centralwidget)
        self.volumeUpButton.setGeometry(QtCore.QRect(60, 450, 121, 31))
        self.volumeUpButton.setObjectName("volumeUpButton")
        self.volumeDownButton = QtWidgets.QPushButton(self.centralwidget)
        self.volumeDownButton.setGeometry(QtCore.QRect(60, 500, 121, 31))
        self.volumeDownButton.setObjectName("volumeDownButton")
        self.muteButton = QtWidgets.QPushButton(self.centralwidget)
        self.muteButton.setGeometry(QtCore.QRect(230, 410, 75, 61))
        self.muteButton.setCheckable(False)
        self.muteButton.setObjectName("muteButton")
        self.powerButton = QtWidgets.QPushButton(self.centralwidget)
        self.powerButton.setGeometry(QtCore.QRect(40, 30, 75, 61))
        self.powerButton.setObjectName("powerButton")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(180, 20, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.title.setFont(font)
        self.title.setTextFormat(QtCore.Qt.AutoText)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(60, 100, 431, 201))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("black.jpg"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setEnabled(True)
        self.horizontalSlider.setGeometry(QtCore.QRect(140, 350, 251, 31))
        self.horizontalSlider.setMaximum(2)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 320, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 380, 16, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(260, 380, 16, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(380, 380, 16, 21))
        self.label_4.setObjectName("label_4")
        Remote.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Remote)
        self.statusbar.setObjectName("statusbar")
        Remote.setStatusBar(self.statusbar)

        self.retranslateUi(Remote)
        QtCore.QMetaObject.connectSlotsByName(Remote)

    def retranslateUi(self, Remote) -> None:
        '''
        This function is used to redefine the GUI. When called upon it resets values
        to default values
        :param Remote: Remote object from class Ui_remote
        :return: -> None
        '''
        _translate = QtCore.QCoreApplication.translate
        Remote.setWindowTitle(_translate("Remote", "MainWindow"))
        self.channelUpButton.setText(_translate("Remote", "Channel +"))
        self.channelDownButton.setText(_translate("Remote", "Channel -"))
        self.volumeUpButton.setText(_translate("Remote", "Volume +"))
        self.volumeDownButton.setText(_translate("Remote", "Volume -"))
        self.muteButton.setText(_translate("Remote", "Mute"))
        self.powerButton.setText(_translate("Remote", "Power"))
        self.title.setText(_translate("Remote", "Remote"))
        self.label.setText(_translate("Remote", "Volume"))
        self.label_2.setText(_translate("Remote", "0"))
        self.label_3.setText(_translate("Remote", "1"))
        self.label_4.setText(_translate("Remote", "2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Remote = QtWidgets.QMainWindow()
    ui = Ui_Remote()
    ui.setupUi(Remote)
    Remote.show()
    sys.exit(app.exec_())
