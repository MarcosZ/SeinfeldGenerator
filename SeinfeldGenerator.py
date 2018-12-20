import os
import subprocess
import random

# vlc path
vlc = "\"C:\\Program Files (x86)\\VideoLan\\VLC\\vlc.exe\""
seinfeldPaths = []
# location of seinfeld root directory on my external
seinfeldRoot = "G:\\Shows\\Seinfeld Complete Box-set x264 Seasons 1 - 9 + Extras DVDRip TSV"
# go to that dir
os.chdir(seinfeldRoot)

# for every directory in that root
for dirName in os.listdir("."):
    season = seinfeldRoot + "\\" + dirName + "\\"

    for fileName in os.listdir(season):
        # makes sure its an .mkv files for VLC
        if fileName.endswith(".mkv"):
            seinfeldPaths.append(season + fileName)

# grabs random value based on number of episodes in the drive
episodeNum = random.randint(0, len(seinfeldPaths) - 1)

# run the random episode in VLC
subprocess.Popen([r"C:\Program Files (x86)\VideoLan\VLC\vlc.exe ", seinfeldPaths[episodeNum]])
