#!/usr/bin/bash
python3 -m unittest discover tests
pycodestyle *.py
pycodestyle models/*.py
