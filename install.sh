sudo apt-get update
sudo apt-get upgrade
sudo apt-get dist-upgrade
sudo apt-get install tightvncserver xrdp python3-dev libffi-dev libssl-dev
sudo pip3 install -U pip
sudo pip3 install virualenv
cd /home/pi
mkdir EpCarProject
cd EpCarProject/
python3 -m venv venv/
source venv/bin/activate
pip install -U pip
pip install twisted[tls,http2] django channels asgi_redis websocket-client
deactivate
