# PILT (Panoramic Interactive Live Tracker)
PILT project want to create an standard to display static and dynamic information over the LG system. We are going to build a system that creates different layers in order to display useful information in the system.

The goal will be create a server that receives online or offline information and translate it into KML, moreover we will represent different uses cases like adding integrations with other Liquid Galaxy projects that has to send KML into the system.


## How to install

###1. Install packages:
```
apt-get install git python-pip ssh sshpass
pip install virtualenvwrapper
```

###2. Get the latest git version and go inside:
```
git clone https://github.com/LiquidGalaxyLAB/PILT
```

###3. Create environment and install dependencies:

```
mkvirtualenv pilt

pip install -r requeriments.txt
```

###4. Run server
```
python manage.py <lg_ip> runserver 0.0.0.0:8000 --noreload
```

Or

```
./pilt-start <lg_ip>
```


