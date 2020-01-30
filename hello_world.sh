#!/bin/bash

# set unique name of each image
image=image-`date +%F_%T`.png
whole_path=/home/username/whole_path_to_the_directory/screen_shooter

# create screenshot with import application
# install ImageMagic’s CLI
import $whole_path/screenshots/$image

# upload the image to dropbox accoutn and get the link to clipboard
python3 $whole_path/transfer_data.py $image | xclip -selection clipboard

# send notification
notify-send -i face-wink "Copied!"

# clear screenshots folder
rm /home/username/whole_path_to_the_directory/screen_shooter/screenshots/*
