# Note Feb 12 2022:
# For now, this is only for local development setup.
# It's not complete.
# Ultimately/eventually I'd like this to also work for production.

sudo apt install python3-venv

cd /vagrant
python3 -m venv venv
venv/bin/pip3 install -r requirements.txt
        
 