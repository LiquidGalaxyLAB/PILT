from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from os import listdir
from os.path import isfile,join
import os

# Create your views here.
from liquidgalaxy.lgCommunication import write_ip, write_kml
from pilt.settings import BASE_DIR


def indexview(request):
    return render(request,'pilt/index.html', {})

def ibriview(request):
    mypath=BASE_DIR
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    folders=[]
    for dirname, dirnames, filenames in os.walk('/tmp/kml/'):
        # print path to all subdirectories first.
        for subdirname in dirnames:
            folders.append(subdirname)
    return render(request,'pilt/ibri.html',{'dirnames':folders})

def ibri_send(request,folder):
    folderKML = BASE_DIR+'/static/ibri/'+folder
    write_kml(folderKML,folder)
    return HttpResponseRedirect(reverse('ibriview'),{})

