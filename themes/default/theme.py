# -*- coding: utf-8 -*-
import os
import resource_default

# ----------------------------------------------------- #
#                   User's template
# ----------------------------------------------------- #
class User(object):
    def __init__(self):
        self.content = open(os.path.dirname(__file__)+'/html/user.html', 'r').read()

    def setName(self, username):
        self.content = self.content.replace("{%USERNAME%}", username)

    def setPhoto(self, photo):
        self.content = self.content.replace("{%USERPHOTO%}", photo)

    def setText(self, text):
        return self.content.replace("{%TEXT%}", text)



# ----------------------------------------------------- #
#                   Guest's template
# ----------------------------------------------------- #
class Guest(object):
    def __init__(self):
        self.content = open(os.path.dirname(__file__)+'/html/guest.html', 'r').read()

    def setName(self, guestname):
        self.content = self.content.replace("{%GUESTNAME%}", guestname)

    def setPhoto(self, photo):
        self.content = self.content.replace("{%GUESTPHOTO%}", photo)

    def setText(self, text):
        return self.content.replace("{%TEXT%}", text)


# ----------------------------------------------------- #
#                   Theme's template
# ----------------------------------------------------- #
class Theme(object):
    def __init__(self):
        html = open(os.path.dirname(__file__)+'/html/theme.html', 'r').read()
        css  = open(os.path.dirname(__file__)+'/css/style.css', 'r').read()
        self.template = html.replace('{%CSS%}', css )
        self.currentHistory = ""
        self.user = User()
        self.guest = Guest()

    def speak(self, data, isuser=True):
        if isuser:
            self.currentHistory += self.user.setText(data)
        else:
            self.currentHistory += self.guest.setText(data)
        return self.template.replace('{%CHAT-HISTORY%}', self.currentHistory)