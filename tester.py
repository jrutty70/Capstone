

import os
import glob
import tables
import numpy as np
import matplotlib.pyplot as plt


def get_all_files(basedir,ext='.h5') :
    """
    From a root directory, go through all subdirectories
    and find all files with the given extension.
    Return all absolute paths in a list.
    """
    allfiles = []
    for root, dirs, files in os.walk(basedir):
        for file in files:
            if file.endswith(ext):
                #allfiles.append(file)
                allfiles.append((os.path.join(root, file),file[:-3]))
                #print(os.path.join(root, file))

    return allfiles

def open_h5_file_read(h5filename):
    """
    Open an existing H5 in read mode.
    Same function as in hdf5_utils, here so we avoid one import
    """
    return tables.open_file(h5filename, mode='r')

#h5 = open_h5_file_read('C:/00/CapDaT/millionsongsubset_full/MillionSongSubset/data/A/C/A/TRACABS128E0786B0B.h5')


basedir = 'c:\\00\\capdat\\millionsongsubset_full\\MillionSongSubset\\data'
#basedir = 'c:\\00\\'

allFiles = get_all_files(basedir)
print(len(allFiles))

for f in allFiles[:10]:
    print(f)

songs = []    
i=0
for f in allFiles[:1000]:
    h5 = open_h5_file_read(f[0])
    songs.append(h5.root.analysis.songs[0])
    h5.close()
    #i+=1
    #print(i)
    #print(h5.root.analysis.songs[0][2])
    #print(f)

print(type(songs[0][0]))
print(type(songs[0]))
print(type(songs))

print((songs[0][0]))
print((songs[0]))
print((songs[:5]))
print(len(allFiles))
print(len(songs))
# for f in allFiles:
#     h5 = open_h5_file_read(f[0])
#     songs.append(h5.root.analysis.songs[0])
#     #print(h5.root.analysis.songs[0][2])
#     #print(f)


xdat =[]
ydat =[]
for s in songs:
    xdat.append(s[3])
    ydat.append(s[27])

plt.plot(xdat) 
plt.plot(ydat) 

plt.show()

plt.plot(xdat) 
plt.show()
plt.plot(ydat) 
plt.show()