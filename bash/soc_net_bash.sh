#!/bin/bash

mdir=$(find ~/ -name "social-network")
cd $mdir
if test -f "requirements.txt"; then
echo "Contents of the file requirements.txt:"
cat requirements.txt
else
echo "There is no file 'requirements.txt' in 'social-network' project"
fi 

