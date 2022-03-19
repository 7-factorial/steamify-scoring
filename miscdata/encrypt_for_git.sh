#! /bin/bash

# exit when any command fails
set -e

echo "Run this in the root dir of the repo."
gpg --output mysite/envconfig.py.gpg --symmetric mysite/envconfig.py 

gpg --output miscdata/judgeData.csv.gpg --symmetric miscdata/judgeData.csv 

gpg --output miscdata/teamData.csv.gpg --symmetric miscdata/teamData.csv