# PILT (Panoramic Interactive Live Tracker)
The main objective of the PILT is display different use cases of the LG to the


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


