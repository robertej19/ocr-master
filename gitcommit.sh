#!/bin/bash

MESS="$1"
echo $MESS

cd client
git add .
git commit -m "$(echo $MESS)"
git push origin master
git status

cd ../server
git add .
git commit -m "$(echo $MESS)"
git push origin master
git status

cd ../utils
git add .
git commit -m "$(echo $MESS)"
git push origin master
git status
