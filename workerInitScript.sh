#!/bin/bash

echo "$1 the url" 

cd C:\Users\Varnit Goel\Documents\Python Scripts

rm -rf .git/
git init
git remote add origin $1
git pull
