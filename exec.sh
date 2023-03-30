#!/bin/bash

# Minecraft Server Scanner [Silverfork]

# Script Dir
SCRIPT_DIR="$(dirname "$(readlink -f "$0")")"
MAIN_DIR="$SCRIPT_DIR/main.py"

sleep 1 && echo "" && echo " ~ Initializing: [${SCRIPT_DIR##*/}] ~ " && echo ""

# Totally legit loading bar
sleep 1 && echo "" && sleep 1 && echo " ~ Starting Command Line Interface ~ " && sleep 1 && echo " ~ (Python3)-(CLI)-(main.py) ~ " && sleep 2 && clear && sleep 1 && echo "" && echo "[=== LOADING ===]" && echo "" && echo -ne '[#]\r' && sleep 0.2 && echo -ne '[##]\r' && sleep 0.2 && echo -ne '[###]\r' && sleep 0.2 && echo -ne '[####]\r' && sleep 0.2 && echo -ne '[#####]\r' && sleep 0.2 && echo -ne '[######]\r' && sleep 0.2 && echo -ne '[#######]\r' && sleep 0.2 && echo -ne '[########]\r' && sleep 0.2 && echo -ne '[#########]\r' && sleep 0.2 && echo -ne '[##########]\r' && sleep 0.2 && echo -ne '[###########]\r' && sleep 0.2 && echo -ne '[############]\r' && sleep 0.2 && echo -ne '[#############]\r' && sleep 0.2 && echo -ne '[##############]\r' && sleep 0.2 && echo -ne '[###############]\r' && sleep 0.2 && echo -ne '[###############]\r' && sleep 0.2 && sleep 1 && clear && sleep 1

# Insert raw paste URL for Readme / Man page
echo " ~ [Manual page from pastebin:] ~ " && sleep 1
curl "https://pastebin.com/raw/2nY0ueHz"

# Execute main.py inside spawned terminal emulator for CLI panel

# Specify all dependencies here
sudo apt install masscan
sudo pip3 install mcstatus
wget https://raw.githubusercontent.com/robertdavidgraham/masscan/master/data/exclude.conf

#python3 main.py
python3 ${MAIN_DIR}
