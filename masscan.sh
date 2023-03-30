#!/bin/bash
#sudo masscan -p25565 0.0.0.0/0 --max-rate 666 --exclude 255.255.255.255 -oL masscan.txt
echo "Simple silver interface for Masscan" && echo ""
echo "Specify port: (25565 by default)"
read port

echo "Please enter the max rate: (Not to melt your router)"
read rate

echo "Please enter the excluded file path: (Don't scan over military networks!)"
read exclude_file

echo "Please enter the output file path: (masscan.txt by default)"
read output_file

clear
echo "=== === === === === === === === === === ==="
sudo masscan -p$port 0.0.0.0/0 --max-rate $rate --exclude $exclude_file -oL $output_file
echo "=== === === === === === === === === === ==="
