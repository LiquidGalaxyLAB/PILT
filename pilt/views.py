from django.shortcuts import render
from django.http import HttpResponse
from os import listdir
from os.path import isfile,join
import os

# Create your views here.

def indexview(request):
    return render(request,'pilt/index.html', {})

def ibriview(request):
    mypath='/Users/marc/Desktop/kml/'
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    print onlyfiles
    folders=[]
    for dirname, dirnames, filenames in os.walk('/Users/marc/Desktop/kml/'):
        # print path to all subdirectories first.
        for subdirname in dirnames:
            folders.append(subdirname)
            print(os.path.join(dirname, subdirname))

        # print path to all filenames.
        #for filename in filenames:
            #print(os.path.join(dirname, filename))

    return render(request,'pilt/ibri.html',{'dirnames':folders})