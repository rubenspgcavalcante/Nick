.PHONY: views
all: resources.py views

resources.py: resources.qrc
	pyrcc4 -py2 resources.qrc -o resources.py

views:
	cd views; \
	make