#!/bin/bash
if ping -c 1 google.com &> /dev/null
then
  echo "Internet connection is active."
else
  echo "No Internet connection."
fi