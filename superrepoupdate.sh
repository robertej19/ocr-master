#!/bin/bash
echo "Good Day Friend, building all submodules while checking out from MASTER branch."

./gitcommit.sh
git submodule update
git submodule foreach git checkout master
git submodule foreach git pull origin master
git add .
git commit -m "change this message to be dynamic"
git push origin master
