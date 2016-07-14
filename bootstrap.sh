#!/usr/bin/env bash

sudo apt-get update
sudo apt-get -y install python-pip
sudo apt-get install python-dev
sudo apt-get install libxml2-dev libxslt1-dev zlib1g-dev
sudo apt-get build-dep python3-lxml
pip install datefinder
