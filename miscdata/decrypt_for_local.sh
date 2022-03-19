#! /bin/bash

# exit when any command fails
set -e

echo "Run this in the root dir of the repo."

gpg --output mysite/envconfig_freshly_decrypted.py --decrypt mysite/envconfig.py.gpg

gpg --output miscdata/judgeData.csv --decrypt miscdata/judgeData.csv.gpg

gpg --output miscdata/teamData.csv --decrypt miscdata/teamData.csv.gpg