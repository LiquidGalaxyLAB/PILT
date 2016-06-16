import os
import time
from pilt.settings import BASE_DIR
import subprocess
from os.path import isfile,join


ip_file = BASE_DIR + '/liquidgalaxy/ipsettings'

def write_ip(ip):
    f = open(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) +
             '/liquidgalaxy/ipsettings', 'w')
    f.write(ip)
    f.close()

def get_ip():
    f = open(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) +'/liquidgalaxy/ipsettings', 'r')
    ip_galaxy = f.read()
    f.close()
    return ip_galaxy

def write_kml(kmlFolder):
    ip_server = get_server_ip()
    os.system("touch /tmp/kmls.txt")
    os.system("rm /tmp/kmls.txt")
    os.system("touch /tmp/kmls.txt")
    file = open("/tmp/kmls.txt", 'w')
    onlyfiles = [f for f in os.listdir(kmlFolder) if isfile(join(kmlFolder, f))]
    for kmlFile in onlyfiles:
        file.write("http://" + str(ip_server)[0:(len(ip_server) - 1)] +":8000/static/ibri/" + kmlFile + "\n")
    send_kml_to_galaxy()


def send_kml_to_galaxy():
    file_path = "/tmp/kmls.txt"
    file_path_slave = "/tmp/kmls_slave.txt"
    server_path = "/var/www/html"
    print("sshpass -p 'lqgalaxy' scp " + file_path + " lg@" + get_ip() +":" + server_path)
    os.system("sshpass -p 'lqgalaxy' scp " + file_path + " lg@" + get_ip() +":" + server_path)




def get_server_ip():
    p = subprocess.Popen(
        "ifconfig eth0 | grep 'inet:' | cut -d: -f2 | awk '{print $1}'",
        shell=True,
        stdout=subprocess.PIPE)
    ip_server = p.communicate()[0]
    return ip_server