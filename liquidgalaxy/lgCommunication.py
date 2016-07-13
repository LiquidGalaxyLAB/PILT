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

def write_kml(kmlFolder,folder):
    print(kmlFolder)
    print(BASE_DIR)

    ip_server = get_server_ip()
    os.system("touch kmls.txt")
    os.system("rm kmls.txt")
    os.system("touch kmls.txt")
    file = open("kmls.txt", 'w')
    onlyfiles = [f for f in os.listdir(kmlFolder) if isfile(join(kmlFolder, f))]
    for kmlFile in onlyfiles:
        file.write("http://" + str(ip_server)[0:(len(ip_server) - 1)] +":8000/static/ibri/"+ folder +"/"+ kmlFile + "\n")
    file.close()
    send_kml_to_galaxy()





def write_kml_airrace(race):
    print(BASE_DIR)
    kmlFolder = BASE_DIR + "/static/airraces/" + race
    print(kmlFolder)
    print"-----"

    ip_server = get_server_ip()
    os.system("touch kmls.txt")
    os.system("rm kmls.txt")
    os.system("touch kmls.txt")
    file = open("kmls.txt", 'w')
    onlyfiles = [f for f in os.listdir(kmlFolder) if isfile(join(kmlFolder, f))]
    for kmlFile in onlyfiles:
        print(kmlFile)
        file.write("http://" + str(ip_server)[0:(len(ip_server) - 1)] +":8000/static/airraces/"+ race +"/"+ kmlFile + "\n")
    file.close()
    send_kml_to_galaxy()


def write_kml_participant(race,participant):

    print participant
    print race
    kmlFolder="static/airraces/"+ race + "/" + participant.kmlpath
    print(kmlFolder)
    ip_server = get_server_ip()
    os.system("touch kmls.txt")
    os.system("rm kmls.txt")
    os.system("touch kmls.txt")
    file = open("kmls.txt", 'w')
    file.write("http://" + str(ip_server)[0:(len(ip_server) - 1)] +":8000/"+ kmlFolder +"\n")
    file.close()
    send_kml_to_galaxy()



def write_kml_race():
    kmlFolder=BASE_DIR+"/static/kml/"
    ip_server = get_server_ip()
    os.system("touch kmls.txt")
    os.system("rm kmls.txt")
    os.system("touch kmls.txt")
    file = open("kmls.txt", 'w')
    onlyfiles = [f for f in os.listdir(kmlFolder) if isfile(join(kmlFolder, f))]
    for kmlFile in onlyfiles:
        file.write("http://" + str(ip_server)[0:(len(ip_server) - 1)] +":8000/static/kml/"+ kmlFile + "\n")
    file.close()
    send_kml_to_galaxy()




def write_idivt_kml():
    ip_server = get_server_ip()
    os.system("touch kmls.txt")
    os.system("rm kmls.txt")
    os.system("touch kmls.txt")
    file = open("kmls.txt", 'w')
    file.write("http://" + str(ip_server)[0:(len(ip_server) - 1)] +":8000/static/idivt/SOLSONA-CONGOST.kml"+ "\n")
    file.close()
    send_kml_to_galaxy()





def send_single_kml(participant):
    print "iouhijgh"
    print participant.kmlpath

    ip_server = get_server_ip()
    os.system("touch kmls.txt")
    os.system("rm kmls.txt")
    os.system("touch kmls.txt")
    file = open("kmls.txt", 'w')
    file.write("http://" + str(ip_server)[0:(len(ip_server) - 1)] +":8000/"+ participant.kmlpath + "\n")
    file.close()
    send_kml_to_galaxy()




def send_kml_to_galaxy():
    file_path = "kmls.txt"
    server_path = "/var/www/html"
    print("sshpass -p 'lqgalaxy' scp " + file_path + " lg@" + get_ip() +":" + server_path)
    os.system("sshpass -p 'lqgalaxy' scp " + file_path + " lg@" + get_ip() +":" + server_path)
    #os.system("sshpass -p 'lqgalaxy' scp -vvv kmls.txt lg@10.160.101.85:/var/www/html")





def get_server_ip():
    p = subprocess.Popen(
        "ifconfig eth0 | grep 'inet addr:' | cut -d: -f2 | awk '{print $1}'",
        shell=True,
        stdout=subprocess.PIPE)
    ip_server = p.communicate()[0]
    return ip_server