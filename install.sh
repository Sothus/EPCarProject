sudo apt-get update
#sudo apt-get upgrade
sudo apt-get dist-upgrade
sudo apt-get install tightvncserver xrdp python3-dev libffi-dev libssl-dev
sudo pip3 install -U pip
sudo pip3 install virualenv
sudo cp rc.local /etc/rc.local
sudo systemctl enable pigpiod.service
python3 -m venv venv/
source venv/bin/activate
pip install -U pip
pip install twisted[tls,http2] django channels asgi_redis websocket-client
deactivate


#Rzeczy potrzebne do zainstalowania Redis-servera z source-code
#sudo apt-get install tcl
#wget http://download.redis.io/redis-stable.tar.gz
#tar xvzf redis-stable.tar.gz
#cd redis-stable/
#make -j4
#make test
#make install
