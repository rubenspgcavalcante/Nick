.PHONY: views
all: resources/resources.py views

resources/resources.py: resources/resources.qrc
	pyrcc4 -py2 resources/resources.qrc -o resources/resources.py
	touch resources/__init__.py

views:
	cd views; \
	make