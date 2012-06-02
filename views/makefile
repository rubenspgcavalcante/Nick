UIPYFILES := $(patsubst %.ui,%.py,$(wildcard *.ui))

all: build

build: $(UIPYFILES) __init__.py

%.py: %.ui
	pyuic4 $< -o $@

__init__.py:
	touch __init__.py