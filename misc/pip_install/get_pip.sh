#!/bin/sh

# get zipped file
wget http://115.29.192.240/get_pip.py.tar

# unzip it
tar -zxvf get_pip.py.tar

# delete zipped file
rm get_pip.py.tar

# install pip
python get_pip.py

# delete get_pip.py
rm get_pip.py


echo pip has been installed, enjoy!
