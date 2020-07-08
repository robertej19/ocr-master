#!/bin/bash

VAR1='"'
MESS="$1"
VAR3="$VAR1$MESS$VAR1"
echo $MESS

cd client
git add .
git commit -m "$VAR3"
git push origin master
git status

cd ../server
git add .
git commit -m "$VAR3"
git push origin master
git status

cd ../utils
git add .
git commit -m "$VAR3"
git push origin master
git status
