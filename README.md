# Mc-Network-scan-Silverfork-
Fork of [robertdavidgraham/masscan] with slight optimization of process runtime &amp; clean IP list output. [excluding version and playerlist from output file]

`# Minecraft-Server-Scanner
Let's you scan the entire internet in a couple of hours and identify all Minecraft servers on IPV4

Installation and running instructions are as follows:
```
sudo apt install masscan (Or distro specific installer command)
wget https://raw.githubusercontent.com/robertdavidgraham/masscan/master/data/exclude.conf
sudo masscan -p25565 0.0.0.0/0 --max-rate <maxrate> --excludefile exclude.conf -oL masscan.txt (Set maxrate to a limit that you are comfortable with and won't melt your router)

pip3 install mcstatus
python3 silverscanner.py

- Now answer the questions of files and specifics that the program asks you (For filtering out public servers you can use my public.txt file but it will probably be a bit outdated by now)
- Hit enter and wait for my program to check and grab the metadata for all the servers found, once this is done you will have a massive amount of servers (A lot of them being private ones) to have some fun with. The output file includes the IP Address, Version and Current Players online of found servers.

**DISCLAIMER: THIS IS FOR EDUCATIONAL PURPOSES ONLY AND I AM NOT RESPONSIBLE FOR ANY MISUSE OF THESE TOOLS!**

FORKED BY SILVERAINOX [Silvershell.INC]`
