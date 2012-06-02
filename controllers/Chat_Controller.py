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
        self.userSpeak = Theme()
        self.userSpeak.setPersistentData("PHOTO", "qrc:/resourcedir/nophoto.png")
        self.userSpeak.setPersistentData("USERNAME", "My Name")
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

    def setTextChatHistory(self, text):
        chatHistory = self.ui.chatHistory
        template = self.userSpeak.setData("TEXT", text)

        if self.talkContent != "":
            self.talkContent = self.talkContent + template
        else:
            self.talkContent = template

        chatHistory.setHtml(self.talkContent, QtCore.QUrl('qrc:/'))