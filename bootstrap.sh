#!/usr/bin/env bash

sudo apt-get update
sudo apt-get -y install python-pip
sudo apt-get -y install libevent-dev python-dev
sudo apt-get -y install libxml2-dev libxslt1-dev zlib1g-dev
sudo apt-get -y build-dep python3-lxml
sudo pip install datefinder
sudo pip install urllib
sudo pip install lxml
sudo pip install regex
sudo pip install python-whois
sudo apt-get install python-dnslib
