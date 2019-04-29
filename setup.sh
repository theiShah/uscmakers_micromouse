
sudo apt-get install build-essential python3-dev python-smbus python3-pip pigpio python-pigpio python3-pigpio

cd ~
mkdir env
python3 -m venv env
source env/bin/activate

sudo pip3 install wheel RPi.GPIO adafruit-mcp3008 networkx matplotlib
