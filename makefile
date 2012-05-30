all:
	pyuic4 views/chat.ui -o views/chat.py
	pyrcc4 -py2 resources.qrc -o resources.py