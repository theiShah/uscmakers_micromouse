
sudo apt-get install build-essential python3-dev python-smbus python3-pip pigpio python-pigpio python3-pigpio

cd ~
mkdir env
python3 -m venv env
source env/bin/activate

pip3 install RPi.GPIO adafruit-mcp3008 networkx