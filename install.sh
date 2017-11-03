#!/bin/bash
#TODO add option to choose type of installation - dev or stand
echo -e "\nUPDATING REPOSITORIES"
apt-get update
if [ $? -ne 0 ]
then
	echo -e "ERROR DURING UPDATING REPOSITORIES"
	echo -e "EXITING..."
	exit 127
fi

echo -e "\nUPGRADING SYSTEM"
apt-get dist-upgrade
if [ $? -ne 0 ]
then
	echo -e "ERROR DURING SYSTEM UPGRADE"
	echo -e "EXITING..."
	exit 127
fi

echo -e "\nINSTALLATION OF TIGHTVNCSERVER"
apt-get install tightvncserver
if [ $? -ne 0 ]
then
	echo -e "ERROR DURING TIGHTVNCSERVER INSTALLATION"
	echo -e "EXITING..."
	exit 127
fi

echo -e "\nINSTALLATION OF XRDP"
apt-get install xrdp
if [ $? -ne 0 ]
then
	echo -e "ERROR DURING XRDP INSTALLATION"
	echo -e "EXITING..."
	exit 127
fi

echo -e "\nINSTALLATION OF PYTHON3-DEV"
apt-get install python3-dev
if [ $? -ne 0 ]
then
	echo -e "ERROR DURING PYTHON3-DEV INSTALLATION"
	echo -e "EXITING..."
	exit 127
fi

echo -e "\nINSTALLATION OF LIBFFI-DEV"
apt-get install libffi-dev
if [ $? -ne 0 ]
then
	echo -e "ERROR DURING LIBFFI-DEV INSTALLATION"
	echo -e "EXITING..."
	exit 127
fi

echo -e "\nINSTALLATION OF LIBSSL-DEV"
apt-get install libssl-dev
if [ $? -ne 0 ]
then
	echo -e "ERROR DURING LIBSSL-DEV INSTALLATION"
	echo -e "EXITING..."
	exit 127
fi

echo -e "\nINSTALLATION OF TCL"
apt-get install tcl
if [ $? -ne 0 ]
then
	echo -e "ERROR DURING TCL INSTALLATION"
	echo -e "EXITING..."
	exit 127
fi

echo -e "\nDOWNLOADING REDIS-STABLE"
wget http://download.redis.io/redis-stable.tar.gz
if [ $? -ne 0 ]
then
	echo -e "ERROR DURING DOWNLOADING REDIS-STABLE"
	echo -e "CHECK YOUR INTERNET CONNECTION AND TRY AGAIN"
	echo -e "EXITING"
	exit 127
fi

echo -e "\nUNPACKING REDIS-STABLE.TAR.GZ"
tar xvzf redis-stable.tar.gz
if [ $? -ne 0 ]
then
	echo -e "ERROR DURING UNPACKING REDIS-STABLE.TAR.GZ"
	echo -e "EXITING..."
	exit 127
fi

echo -e "\nCHANGING DIRECTORY TO redis-stable/"
cd redis-stable/

echo -e "\nCOMPILING REDIS"
make
if [ $? -ne 0 ]
then
	echo -e "ERROR DURING COMPILATION REDIS"
	echo -e "EXITING..."
	exit 127
fi

echo -e "\nINSTALLATION REDIS"
make install
if [ $? -ne 0 ]
then
	echo -e "ERROR DURING REDIS INSTALLATION"
	echo -e "EXITING..."
	exit 127
fi

echo -e "\nEXITING DIRECTORY redis-stable/"
cd ..

echo -e "\nREMOVING REDIS-STABLE.TAR.GZ"
rm redis-stable.tar.gz
if [ $? -ne 0 ]
then
	echo -e "ERROR DURING REMOVING FILE"
	echo -e "EXITING..."
	exit 127
fi

echo -e "\nREMOVING REDIS-STABLE DIRECTORY"
rm redis-stable -r -v
if [ $? -ne 0 ]
then
	echo -e "ERROR DURING REMOVING DIRECTORY"
	echo -e "EXITING..."
	exit 127
fi

echo -e "\nUPGRADING PIP"
pip3 install -U pip
if [ $? -ne 0 ]
then
	echo -e "ERROR DURING UPDATING PIP"
	echo -e "EXITING..."
	exit 127
fi

echo -e "\nINSTALLING VIRTUALENV"
pip3 install virtualenv
if [ $? -ne 0 ]
then
	echo -e "ERROR DURING INSTALLING VIRTUALENV"
	echo -e "EXITING..."
	exit 127
fi

#TODO change it to append line to rc.local
echo -e "\nCOPYING RC.LOCAL"
cp rc.local /etc/rc.local
if [ $? -ne 0 ]
then
	echo -e "ERROR DURING COPYING RC.LOCAL FILE"
	echo -e "EXITING..."
	exit 127
fi

echo -e "\nADDING PIGPIOD.SERVICE TO AUTOSTART"
systemctl enable pigpiod.service
if [ $? -ne 0 ]
then
	echo -e "ERROR DURING ADDING PIGPIOD.SERVICE TO AUTOSTART"
	echo -e "EXITING..."
	exit 127
fi

echo -e "\nCREATING VIRTUAL ENVIRONMENT"
python3 -m venv venv/
if [ $? -ne 0 ]
then
	echo -e "ERROR DURING CREATING VIRTUAL ENVIRONMENT FOR PYTHON"
	echo -e "EXITING..."
	exit 127
fi

echo -e "\nACTIVATING VIRTUALENVIRONMENT"
source venv/bin/activate
if [ $? -ne 0 ]
then
	echo -e "ERROR DURING ACTIVATING VIRTUALENV"
	echo -e "EXITING..."
	exit 127
fi

echo -e "\nUPDATING PIP"
pip3 install -U pip
if [ $? -ne 0 ]
then
	echo -e "ERROR DURING UPDATING PIP IN VIRTUALENV"
	echo -e "DEACTIVATING VIRTUALENV"
	deactivate
	echo -e "EXITING..."
	exit 127
fi

echo -e "\nINSTALLING TWISTED"
pip3 install twisted[tls,http2]
if [ $? -ne 0 ]
then
	echo -e "ERROR DURING TWISTED INSTALLATION"
	echo -e "DEACTIVATING VIRTUALENV"
	deactivate
	echo -e "EXITING..."
	exit 127
fi

echo -e "\nINSTALLING DJANGO"
pip3 install django
if [ $? -ne 0 ]
then
	echo -e "ERROR DURING DJANGO INSTALLATION"
	echo -e "DEACTIVATING VIRTUALENV"
	deactivate
	echo -e "EXITING..."
	exit 127
fi

echo -e "\nINSTALLING CHANNELS"
pip3 install channels
if [ $? -ne 0 ]
then
	echo -e "ERROR DURING DJANGO CHANNELS INSTALLATION"
	echo -e "DEACTIVATING VIRTUALENV"
	deactivate
	echo -e "EXITING..."
	exit 127
fi

echo -e "\nINSTALLING ASGI_REDIS"
pip3 install asgi_redis
if [ $? -ne 0 ]
then
	echo -e "ERROR DURING ASGI_REDIS INSTALLATION"
	echo -e "DEACTIVATING VIRTUALENV"
	deactivate
	echo -e "EXITING..."
	exit 127
fi

echo -e "\nINSTALLING WEBSOCKET-CLIENT"
pip3 install websocket-client
if [ $? -ne 0 ]
then
	echo -e "ERROR DURING WEBSOCKET-CLIENT INSTALLATION"
	echo -e "DEACTIVATING VIRTUALENV"
	deactivate
	echo -e "EXITING..."
	exit 127
fi

echo -e "INSTALLATION SUCCESFULL"
echo -e "DEACTIVATING VIRTUALENV"
deactivate
echo -e "EXITING..."
exit 0

