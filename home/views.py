from subprocess import run, PIPE
import sys
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'home.html')


def sender(request):
    return render(request, 'sender.html')


def receiver(request):
    return render(request, 'receiver.html')


def chatbot(request):
    return render(request, 'chatbot.html')


def ocr(request):
    return render(request, 'ocr.html')

 # import requests


def button(request):
    return render(request, 'home.html')


def external(request):
    inp = request.POST.get('param')
    # out= run([sys.executable,'//mnt//e//work//djnago_testing//test.py',inp],shell=False,stdout=PIPE)
    out = run([sys.executable, '..//customercare//chatbot//chatgui.py'],
              shell=False, stdout=PIPE)
    print(out)

    return render(request, 'chatbot.html', {'data1': out.stdout})


def externalTwo(request):
    inp = request.POST.get('ip')
    out = run([sys.executable, 'F://New folder//intern_project//ocr//ocr_scanner.py', inp],
              shell=False, stdout=PIPE)
    print(out)

    return render(request, 'home.html', {'data1': out.stdout})
