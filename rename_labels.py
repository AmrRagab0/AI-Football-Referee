

import os

# set the path to the directory
path = './2014-2015'

# loop over subdirectories
for root, dirs, files in os.walk(path):
    for file in files:
        # check if the file is named "labels-V2.json"
        if file == 'Labels-v2.json':
            # rename the file to "5-Labels-V2.json"
            os.rename(os.path.join(root, file), os.path.join(root, '5-Labels-V2.json'))
