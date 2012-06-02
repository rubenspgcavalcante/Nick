# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, uic, QtCore
from views import chat
from themes.default.theme import Theme
from resources import resources

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Main(object):
    def run(self):
        app = QtGui.QApplication(sys.argv)
        window = Chat_Controller()
        window.show()
        sys.exit(app.exec_())


class Chat_Controller(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = chat.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.chatInput.installEventFilter(self)
        #Loading theme and things like photos and names
        self.theme = Theme()
        self.theme.user.setPhoto("qrc:/resourcedir/nophoto.png")
        self.theme.user.setName("My Name")
        self.theme.guest.setPhoto("qrc:/resourcedir/nophoto.png")
        self.theme.guest.setName("Guest's Name")
        self.talkContent = ""

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.KeyPress:
            if event.key() == QtCore.Qt.Key_Return:
                self.getTextReturned(obj, event)
                return True
        return False

    def getTextReturned(self, obj, event):
        text = obj.toPlainText()
        obj.setText("")
        self.setTextChatHistory(text)
        pass

    def setTextChatHistory(self, text, isuser=true):
        chatHistory = self.ui.chatHistory
        speakHtml = self.theme.speak(text, isuser)

        chatHistory.setHtml(speakHtml, QtCore.QUrl('qrc:/'))