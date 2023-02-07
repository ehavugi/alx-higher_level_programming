#!/usr/bin/bash
python3 -m doctest -v tests/*
pycodestyle *.py
