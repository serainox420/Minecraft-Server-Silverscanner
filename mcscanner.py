#// SUPER SILVER SCANNER FOR Minecrap
#// Excludes version and players from output file.

from mcstatus import MinecraftServer
import os
import threading
import time

masscan = []

print('Silver fork of deathsiefat scanner')


print('       /"-.                      ')
print('      / \--`.  __..-,O           ')
print('     :   \ --  _..- .            ')
print('     |    . .-   .  .            ')
print('     :     .     . .             ')
print('      \      .  /  ..            ')
print('       \       .     .           ')
print('         ,        .   \          ')
print('       ,|, .         -.\         ')
print('       .||   -.  __..-"          ')
print('       |  |                      ')
print('       |__|                      ')
print('       /||\                      ')
print('      //||\\                     ')
print('     // || \\                    ')
print('  __//__||__\\__                 ')
print('  --------------                ')
                   

time.sleep(1)

inputfile = input('Raw server ips file? (Including the .txt): ')

outputfile = input('File name to save output into? (Including the .txt): ')

publicserverlist = input('Public ips to exclude? (Including the .txt): ')

searchterm = input('Target game version? (null=all): ')

outfile = open(outputfile, 'a+')
outfile.close

fileHandler = open (inputfile, "r")
listOfLines = fileHandler.readlines()
fileHandler.close()

for line in listOfLines:
    if line.strip()[0] != "#":
        masscan.append(line.strip().split(' ',4)[3])



def split_array(L,n):
    return [L[i::n] for i in range(n)]


threads = int(input('Threads to use (Recommended 20): '))

time.sleep(2)

if len(masscan) < int(threads):
    threads = len(masscan)


split = list(split_array(masscan, threads))

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        print ("Starting Thread " + self.name)
        print_time(self.name)
        print ("Exiting Thread " + self.name)

def print_time(threadName):
    for z in split[int(threadName)]:
        if exitFlag:
            threadName.exit()
        try:
            ip = z
            server = MinecraftServer(ip,25565)
            status = server.status()
        except:
            print("No Server Found:" + ip)
        else:
            print("Server:" + ip)
            
            if searchterm in status.version.name:
                with open(outputfile) as f:
                    if ip not in f.read():
                        with open(publicserverlist) as g:
                            if ip not in g.read():
                                text_file = open(outputfile, "a")
                                text_file.write(ip)
#                                + " " + status.version.name.replace(" ", "_") + " " + str(status.players.online)
                                text_file.write(os.linesep)
                                text_file.close()


for x in range(threads):
    thread = myThread(x, str(x)).start()
