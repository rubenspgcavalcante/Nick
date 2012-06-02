QRCPYFILES := $(patsubst %.qrc,%.py,$(wildcard *.qrc))
PYVER = -py2

all: build

build: $(QRCPYFILES) __init__.py

%.py: %.qrc
	pyrcc4 $(PYVER) $< -o resource_$@

__init__.py:
	touch __init__.py