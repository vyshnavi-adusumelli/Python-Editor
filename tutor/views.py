from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
import shlex, subprocess
import hashlib
from django.core.files import File
from django.core.files.storage import FileSystemStorage
from django.conf import settings


def visualize(request):
    if request.POST.get('code'):
        txt = request.POST.get('code')
    else:
        txt = " "
        print(txt)
    with open("out.py", "w") as f1:
        f1.write(txt)
        #f.close()
    p2 = subprocess.Popen('python3 out.py', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    tx2 = ""
    for line in p2.stdout.readlines():
        print(line)
        tx2 = tx2 + str(line, 'utf-8') 
    retval = p.wait()
    rendered = render(request, "visualize.html", {'output':txt, 'output1':tx2})
    return HttpResponse(rendered)

"""    p1 = subprocess.Popen('python2 pg_logger.py out.py', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    tx1 = ""
    for line in p1.stdout.readlines():
        print(line)
        tx1 = tx1 + str(line, 'utf-8') 
    with open("output.py", "w") as f2:
        f2.write(tx1)
        
    p = subprocess.Popen('python3 astsample.py', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    tx = ""
    for line in p.stdout.readlines():
        print(line)
        tx = tx + str(line, 'utf-8') 
    retval = p.wait()
    rendered = render(request, "visualize.html", {'output':tx, 'output1':txt, 'output2':tx2})
    return HttpResponse(rendered)
"""
# Create your views here.
