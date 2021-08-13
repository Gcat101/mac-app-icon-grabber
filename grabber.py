# Modules
import os, shutil
from PIL import Image

# Find the app
for file in os.listdir():
    filename, file_extension = os.path.splitext('/' + file)
    if (file_extension == ".app"):
        path = rf'{file}/Contents/Resources'
        break

# Find the icon
for file in os.listdir(path=path):
    filename, file_extension = os.path.splitext('/' + file)
    if (file_extension == ".icns"):
        icns = file
        break

# Copy the icon
temp = shutil.copyfile(rf'{path}/{icns}', r'temp.icns')

# Convert the icon
output = Image.open(temp)
output.save('output.png') # Save the .png

# Delete the icon (.icns)
os.remove(temp)