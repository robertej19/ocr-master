#!/bin/bash
echo "Updating everything"

VAR1='"'
MESS="$1"
VAR3="$VAR1$MESS$VAR1"
echo $MESS

#./gitcommit.sh $VAR3
#git submodule update
#git submodule foreach git checkout master
#git submodule foreach git pull origin master
git add .
git commit -m "$(echo $MESS)"
git push origin master
