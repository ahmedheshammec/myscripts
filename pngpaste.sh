#!/bin/bash
Location=$1
eval Location="$Location"     # expand ~ character
cd "$Location"
pngpaste image.png
