#!/bin/bash

# Update and install dependencies
sudo apt-get update
sudo apt-get install -y python3-pip python3-dev
sudo pip3 install -r requirements.txt
